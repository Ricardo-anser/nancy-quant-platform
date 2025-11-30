from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('me/', views.UserDetailView.as_view(), name='user-detail'),
]