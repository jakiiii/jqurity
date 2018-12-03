from django.urls import path
from .views import HomeContentListView


urlpatterns = [
    path('', HomeContentListView.as_view(), name='home')
]
