from django.contrib import admin
from purchase.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass
