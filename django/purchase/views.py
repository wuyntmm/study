from .models import Purchase
from django.views.generic import ListView, DetailView
from rest_framework import generics
from .serializers import *


class PurchaseList(ListView):
    model = Purchase


class PurchaseDetail(DetailView):
    model = Purchase

class APIPurchase(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer