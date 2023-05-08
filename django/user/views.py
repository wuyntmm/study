from user.models import User
from django.views.generic import ListView, CreateView, DetailView
from .forms import UserForm
from django.urls import reverse_lazy
from rest_framework import generics, filters
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
import django_filters

class ListUser(ListView):
    model = User


class DetailUser(DetailView):
    model = User


class CreateUser(CreateView):
    model = User
    template_name = 'user/add_user.html'
    form_class = UserForm
    success_url = reverse_lazy('user-list')


class APIUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['contains'],
            'last_name': ['contains'],
            'age': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class UserPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filterset_class = UserFilter
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['age', ]
    pagination_class = UserPaginator

    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]