from django.urls import path
from .views import get_purchases

urlpatterns = [
    path('', get_purchases, name='purchase')
]