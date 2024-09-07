from django.db import models

from app.user.models import User


class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transaction"
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return f"Transaction from {self.sender.email} to {self.receiver.email} - {self.amount}"


class CsinCoinModel(models.Model):
    turnover = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Оборот")
    number_coins = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Количество монет")
    well = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Курс", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "csin_coin_model"
        verbose_name = "Курс CsinCoin"
        verbose_name_plural = "Курсы CsinCoin"

    def __str__(self):
        return f"{self.turnover}-{self.number_coins}-{self.well}"

    def save(self, *args, **kwargs):
        if self.number_coins > 0:
            self.well = self.turnover / self.number_coins
        super().save(*args, **kwargs)
