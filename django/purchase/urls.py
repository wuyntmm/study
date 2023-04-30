from django.urls import path
from .views import PurchaseList, PurchaseDetail

urlpatterns = [
    path('', PurchaseList.as_view(), name='purchase-list'),
    path('<int:pk>', PurchaseDetail.as_view(), name='purchase-detail'),
]