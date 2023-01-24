from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cmms_app'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="cmms_app/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),
]