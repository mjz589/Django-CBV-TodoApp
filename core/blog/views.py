from django.shortcuts import render

from django.views.generic.base import TemplateView ,RedirectView
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def indexView(request):
    """
    a function based view to show index page
    """
    return render(request, 'index.html')

class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "alias"
        context["posts"] = Post.objects.all()
        return context
    
class PostList(LoginRequiredMixin, ListView):
    """
    >>>> model, queryset and def get_queryset do the same thing (fetch data from model/database) <<<<
    # model = Post
    # queryset = Post.objects.all()
    """
    # if you don't like the name of object_list for your objects:
    context_object_name = 'posts'
    paginate_by = 2
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts
    
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
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
    

"""  
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""  

# create a new post ../blog/post_form.html
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm # the upper line does the same job but this line fetchs form from forms.py
    success_url = '/blog/post/'

    # automatically detect author
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

# edit/update a new post ../blog/post_form.html
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

# delete a post ../blog/post_confirm_delete.html
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'

