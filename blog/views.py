from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Blog
from post.models import Post
from category.models import Category, SubCategory
from about.models import AboutModel, SocialModel


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    context_object_name = 'home_content'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['banner_img'] = Blog.objects.all()[:1]
        context['about_me'] = AboutModel.objects.all()[:1]
        context['social_link'] = SocialModel.objects.all()[:1]
        context['category_list'] = Category.objects.all()
        context['sub_category'] = SubCategory.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = '{}'.format(self.get_object().title)
        context['social_link'] = SocialModel.objects.all()[:1]
        category_post = Post.get_category()
        context['related_post'] = Post.objects.filter(category__sub_category=self.category_post).exclude(id=Post)[:3]
        return context

    # name = product.get_category()
    # relateds = ProductBasic.objects.filter(category__name=name).exclude(id=product.id)[:5]
