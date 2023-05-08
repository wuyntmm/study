from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list', ListUser.as_view(), name='user-list'),
    path('<int:pk>', DetailUser.as_view(), name='user-detail'),
    path('add/', CreateUser.as_view(), name='user-create'),
    path('apiuser', APIUser.as_view(), name='api-user'),
]

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
