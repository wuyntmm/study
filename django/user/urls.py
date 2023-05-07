from django.urls import path
from .views import ListUser, DetailUser, CreateUser, APIUser

urlpatterns = [
    path('', ListUser.as_view(), name='user-list'),
    path('<int:pk>', DetailUser.as_view(), name='user-detail'),
    path('add/', CreateUser.as_view(), name='user-create'),
    path('apiuser', APIUser.as_view(), name='api-user'),
]
