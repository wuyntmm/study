from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list', PurchaseList.as_view(), name='purchase-list'),
    path('<int:pk>', PurchaseDetail.as_view(), name='purchase-detail'),
    path('apipurchase', APIPurchase.as_view(), name='api-purchase'),
]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls
