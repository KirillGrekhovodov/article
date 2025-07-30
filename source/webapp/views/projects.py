from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from webapp.forms import ProjectForm
from webapp.forms.projects import AddUsersInProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = "projects"
    ordering = ['-created_at']


class CreateProjectView(PermissionRequiredMixin, CreateView):
    template_name = 'projects/create_project.html'
    form_class = ProjectForm
    permission_required = 'webapp.add_project'
    success_url = reverse_lazy("webapp:project-list")

    def form_valid(self, form):
        project = form.save()
        project.users.add(self.request.user)
        return redirect('webapp:index')


class DetailProjectView(DetailView):
    template_name = 'projects/detail_project.html'
    model = Project


class AddUserInProjectView(PermissionRequiredMixin, UpdateView):
    template_name = 'projects/add_users_in_project.html'
    permission_required = 'webapp.add_users_in_project'
    model = Project
    form_class = AddUsersInProjectForm

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse('webapp:project-detail', kwargs={'pk': self.get_object().pk})

    def get_form_kwargs(self):
        result = super().get_form_kwargs()
        result['user'] = self.request.user
        return result