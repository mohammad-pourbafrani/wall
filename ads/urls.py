from django.urls import path
from . import views

urlpatterns = [
    path("list", views.AdListView.as_view(), name="list"),
    path("create", views.AdCreateView.as_view(), name="create"),
]
