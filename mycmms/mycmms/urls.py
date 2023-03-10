"""mycmms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name="cmms_app/login.html"), name='login'),
    path('home', views.HomePage.as_view(), name='home'),
    path('cmms_app/', include('cmms_app.urls', namespace='cmms_app')),
    path('cmms_app/', include('django.contrib.auth.urls')),
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('metrics/', include('metrics.urls', namespace='metrics')),
]
