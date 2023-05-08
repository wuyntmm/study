from .models import Book
from django.views.generic import ListView, CreateView, DetailView
from .forms import BookForm
from django.urls import reverse_lazy
from rest_framework import generics, filters
from .serializers import BookSerializer
import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


class APIBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBook(CreateView):
    model = Book
    template_name = 'book/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('book-list')


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['contains'],
            'author': ['contains'],
            'price': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class BookPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', ]
    pagination_class = BookPagination

    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]