from django.http import HttpResponse, JsonResponse
from user.models import User

def get_users(request):
    users = User.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)