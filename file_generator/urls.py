from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<str:filename>/<int:dataCount>", views.generate_random_file, name="gen_file"),
]
