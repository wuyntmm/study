from celery import shared_task
from user.models import User
from purchase.models import Purchase


@shared_task
def some_text():
    print('Some text here')


@shared_task
def print_user_count():
    users = User.objects.all()
    print(f'Users: {users.count()}')


@shared_task
def purchase_for_id(user_id):
    purchases = Purchase.objects.filter(user_id=user_id)
    print(f'User #{user_id} has done {purchases.count()} purchases')
