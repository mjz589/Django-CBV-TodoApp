from django.shortcuts import render

from django.views.generic.base import TemplateView ,RedirectView
from django.views.generic import ListView
from .models import *
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
    
class PostList(ListView):
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
    

    
