from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreatePostFrom

from about.models import SocialModel
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
        context['social_link'] = SocialModel.objects.all()[:1]
        return context


class UserInfoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserInfoChangeForm
    template_name = 'profiles/update_user_info.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Info"
        context['social_link'] = SocialModel.objects.all()[:1]
        return context

    def get_success_url(self):
        return reverse('profile')


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5
    login_url = '/account/login/'
    context_object_name = 'post_list'
    template_name = 'profiles/post_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Posts'
        context['social_link'] = SocialModel.objects.all()[:1]
        return context

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class UserPostCreateView(LoginRequiredMixin, CreateView):
    pass
    form_class = CreatePostFrom
    login_url = '/account/login/'
    success_url = '/profile/posts/'
    template_name = 'profiles/create_post.html'

    # def get(self, request):
    #     obj = render(request, self.template_name, {"post": self.form_class})
    #     return obj

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Post'
        return context
