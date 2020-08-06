from django.urls import path, include
from .views import signup, profile, profile_edit

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),

]