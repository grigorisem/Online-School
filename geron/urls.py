from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lessons", views.lessons_view, name="lessons"),
    path("profile", views.profile_view, name="profile"),
]