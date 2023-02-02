from django.urls import path
from . import views

app_name = "todoapp"

urlpatterns = [
    path("list/", views.TodoListView.as_view(), name="list"),
    path("detail/<slug>/", views.TodoDetailView.as_view(), name="detail"),
]