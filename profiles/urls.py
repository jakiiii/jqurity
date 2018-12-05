from django.urls import path

from .views import (
    ProfileView,
    UserInfoUpdateView,
    UserPostListView
)


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('posts/', UserPostListView.as_view(), name='user-post'),
    path('update/', UserInfoUpdateView.as_view(), name='update-info'),
]
