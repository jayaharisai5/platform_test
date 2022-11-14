from django.urls import path, include
from . import views

urlpatterns = [
    path('s3', views.s3, name="s3"),
    path('s3_show_csv', views.s3_show_csv, name="s3_show_csv")
]