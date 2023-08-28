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

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts
    

    
