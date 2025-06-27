from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

from webapp.models import Article, Blog


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'index.html', {"articles": articles})


def create_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        blog_id = request.POST.get('blog_id')
        # blog = Blog.objects.filter(title=blog_title).first()
        article = Article.objects.create(title=title, content=content, author=author, blog_id=blog_id)

        return redirect("article-detail", pk=article.pk)
    else:
        blogs = Blog.objects.all()
        return render(request, 'create_article.html', {"blogs": blogs})


def article_detail(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'detail_article.html', {"article": article})

