from .models import Purchase
from django.views.generic import ListView, DetailView


class PurchaseList(ListView):
    model = Purchase


class PurchaseDetail(DetailView):
    model = Purchase
