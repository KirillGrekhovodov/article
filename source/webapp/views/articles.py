from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from django.views.generic import FormView, ListView, DetailView

from webapp.forms import ArticleForm, SearchForm
from webapp.forms.articles import DeleteArticleForm

from webapp.models import Article


class ArticleListView(ListView):
    template_name = 'articles/index.html'
    model = Article
    context_object_name = "articles"
    ordering = ['-created_at']
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.tag = self.request.GET.get('tag')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value))
        if self.tag:
            queryset = queryset.filter(tags__title=self.tag).distinct()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        query_params = {}
        if self.search_value:
            query_params.update({"search": self.search_value})
            result['search'] = self.search_value
        if self.tag:
            query_params.update({"tag": self.tag})
            result['tag'] = self.tag

        if query_params:
            result['query'] = urlencode(query_params)
        return result

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


class CreateArticleView(FormView):
    template_name = 'articles/create_article.html'
    form_class = ArticleForm

    def form_valid(self, form):
        article = form.save()
        return redirect("article-detail", pk=article.pk)


class UpdateArticleView(FormView):
    template_name = 'articles/update_article.html'
    form_class = ArticleForm

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.article
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def form_valid(self, form):
        form.save()
        return redirect("article-detail", pk=self.article.pk)


def delete_article(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = DeleteArticleForm(request.POST, origin_title=article.title)
        if form.is_valid():
        # title = request.POST.get('title')
        # if title == article.title:
            article.delete()
            return redirect("index")
        # form.errors['title'] = ["Не совпадают названия"]
        return render(request, 'articles/delete_article.html', {"article": article, "form": form})
    else:
        form = DeleteArticleForm()
        return render(request, 'articles/delete_article.html', {"article": article, "form": form})


class DetailArticleView(DetailView):
    template_name = 'articles/detail_article.html'
    model = Article


    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['comments'] = self.object.comments.order_by('-created_at')
        return result
