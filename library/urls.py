from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_janrs, name="all_janr"),
    path("<int:pk>/", views.get_book, name='detail_book'),
    path("create/", views.create_book, name='create_book'),
]