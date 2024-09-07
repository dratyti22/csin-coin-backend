from django.contrib import admin

from app.wallet.models import Transaction, CsinCoinModel


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["amount", "transaction_date"]
    list_filter = ["id"]
    search_fields = ["id"]


@admin.register(CsinCoinModel)
class CsinCoinModelAdmin(admin.ModelAdmin):
    list_display = ["turnover", "number_coins", "well"]
    list_filter = ["turnover", "number_coins", "well"]
