from django.urls import path
from .views import ListUser, DetailUser,CreateUser

urlpatterns = [
    path('', ListUser.as_view(), name='user-list'),
    path('<int:pk>', DetailUser.as_view(), name='user-detail'),
    path('add/', CreateUser.as_view(), name='user-create'),
]
