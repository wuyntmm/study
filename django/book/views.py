from django.http import HttpResponse, JsonResponse
from .models import Book


def get_books(request):
    users = Book.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)
