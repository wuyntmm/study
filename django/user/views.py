from django.http import HttpResponse, JsonResponse
from user.models import User
from django.views.generic import ListView, CreateView, DetailView
from .forms import UserForm
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import UserSerializer


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
