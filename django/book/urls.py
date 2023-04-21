from django.urls import path
from .views import get_books

urlpatterns = [
    path('', get_books, name='book')
]