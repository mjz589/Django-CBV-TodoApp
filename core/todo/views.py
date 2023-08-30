from typing import Any
from django.db import models
from django.shortcuts import render, redirect

from django.views.generic.base import (TemplateView ,RedirectView)
from django.views.generic import (
            View,
            ListView,
            FormView,
            CreateView,
            UpdateView,
            DeleteView)
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile
from django.urls import reverse_lazy
# Create your views here.

# show todo list ../todo/task_list.html
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/task_list.html'
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    context_object_name = 'tasks'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        if not context.get('is_paginated', False):
            return context
        # Custom Pagination
        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_no = current_page.number

        if num_pages <= 5 or page_no <= 3:  # case 1 and 2
            pages = [x for x in range(1, min(num_pages + 1, 5))]
        elif page_no > num_pages - 3:  # case 4
            pages = [x for x in range(num_pages - 4, num_pages + 1)]
        else:  # case 3
            pages = [x for x in range(page_no - 2, page_no + 3)]

        context.update({'pages': pages})
        return context
    

# create a task ../todo/task_form.html
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    success_url = reverse_lazy("task_list")
    template_name = 'todo/task_create.html'
    # automatically detect author
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)


# update/edit a task ../todo/task_form.html
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    context_object_name = "task"
    template_name = 'todo/task_update.html'
    success_url = reverse_lazy("task_list")
    form_class = UpdateTaskForm
    


# delete  a task ../todo/task_confirm_delete.html
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)



# mark a task as completed 
class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("task_list")
    context_object_name = "task"

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs.get('pk'))
        task.complete = True
        task.save()
        return redirect(self.success_url)
