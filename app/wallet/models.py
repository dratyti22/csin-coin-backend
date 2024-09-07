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
