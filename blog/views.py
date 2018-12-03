from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from post.models import Post
from category.models import Category, SubCategory


# Create your views here.
class HomeContentListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'home_content'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.all()
        return context
