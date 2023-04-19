from django.http import HttpResponse, JsonResponse
from .models import Purchase

def get_purchases(request):
    users = Purchase.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)