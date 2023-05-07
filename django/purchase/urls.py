from django.urls import path
from .views import *

urlpatterns = [
    path('', PurchaseList.as_view(), name='purchase-list'),
    path('<int:pk>', PurchaseDetail.as_view(), name='purchase-detail'),
    path('apipurchase', APIPurchase.as_view(), name='api-purchase'),
]