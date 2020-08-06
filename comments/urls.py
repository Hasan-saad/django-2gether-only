from django.urls import path, include
from .views import comments_user

app_name = 'comments'

urlpatterns = [
    path('comments', comments_user, name='comments_user'),


]