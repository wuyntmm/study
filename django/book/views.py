from .models import Book
from django.views.generic import ListView, CreateView, DetailView
from .forms import BookForm
from django.urls import reverse_lazy


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


class CreateBook(CreateView):
    model = Book
    template_name = 'book/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('book-list')
