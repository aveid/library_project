from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_janrs, name="all_janr"),
    path("<int:pk>/", views.get_book, name='detail_book'),
]