from django.urls import path
from .views import AdListView

urlpatterns = [
    path("list", AdListView.as_view(), name="list"),
]
