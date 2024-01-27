from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import SignUpForm, TaskForm,CategoryForm

from accounts.models import Category, Task
# Create your views here.


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['categories'] = Category.objects.filter(user=self.request.user)
        
        return context



class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    success_url = '/'
    template_name = 'task_create.html'
    form_class = TaskForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    success_url = '/'
    template_name = 'task_create.html'
    form_class = TaskForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdateView, self).form_valid(form)
    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'view_task.html'


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    success_url = '/'
    model = Task
    template_name = 'delete_task.html'


class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'list_task.html'


class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    success_url = '/'
    template_name = 'category_create.html'
    form_class = CategoryForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)


    
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = '/auth/login'
    template_name = 'registration/register.html'
    


    


