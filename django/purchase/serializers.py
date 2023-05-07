from rest_framework import serializers
from .models import *


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ('user', 'book', 'date', )