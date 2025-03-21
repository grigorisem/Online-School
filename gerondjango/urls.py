"""
URL configuration for gerondjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import registration_view
from geron import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("geron.urls")),
    path("lessons", views.lessons_view, name="lessons"),
    path("profile", views.profile_view, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register", registration_view, name="register")
]
