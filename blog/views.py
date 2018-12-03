from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Blog
from post.models import Post
from category.models import Category, SubCategory
from about.models import AboutModel, SocialModel


# Create your views here.
class HomeContentListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'home_content'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['banner_img'] = Blog.objects.all()[:1]
        context['about_me'] = AboutModel.objects.all()[:1]
        context['social_link'] = SocialModel.objects.all()[:1]
        context['category_list'] = Category.objects.all()
        return context
