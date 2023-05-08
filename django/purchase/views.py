from .models import Purchase
from django.views.generic import ListView, DetailView
from rest_framework import generics, filters
from .serializers import *
import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

class PurchaseList(ListView):
    model = Purchase


class PurchaseDetail(DetailView):
    model = Purchase

class APIPurchase(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user': ['exact'],
            'book': ['exact'],
            'date': ['gte', 'lte', 'gt', 'lt', 'exact']
        }

class PurchasePaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    filterset_class = PurchaseFilter
    search_fields = ['user', 'book']
    ordering_fields = ['date', ]
    pagination_class = PurchasePaginator

    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]