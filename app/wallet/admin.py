from django.contrib import admin

from app.wallet.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["amount", "transaction_date"]
    list_filter = ["id"]
    search_fields = ["id"]
