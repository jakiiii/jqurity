from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import UserInfoChangeForm
from accounts.models.user_models import User
from post.models import Post


# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profiles/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Profile'
        return context


class UserInfoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserInfoChangeForm
    template_name = 'profiles/update_user_info.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Info"
        return context

    def get_success_url(self):
        return reverse('profile')


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5
    login_url = '/login/'
    context_object_name = 'post_list'
    template_name = 'profiles/post_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Posts'
        return context

    # def get_queryset(self):
    #     return Post.objects.filter(owner=self.request.user)
