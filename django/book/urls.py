from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list/', BookList.as_view(), name='book-list'),
    path('<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('add/', CreateBook.as_view(), name='book-create'),
    path('apibook', APIBook.as_view(), name='api-book')
]

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns += router.urls