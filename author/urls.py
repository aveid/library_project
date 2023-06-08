from django.urls import path
from . import views


urlpatterns = [
    path("", views.AuthorView.as_view(), name="author"),
    path("<int:pk>/", views.DetailUpdateView.as_view(), name="update")
]