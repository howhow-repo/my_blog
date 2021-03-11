from django.urls import path
from . import views

urlpatterns = [
    path("",views.profile),
    path("post/",views.index),
    path("post/<int:post_slug>",views.post),
]