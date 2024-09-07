from django.urls import path

from app.wallet.views import TopUpBalanceView, StatusAdminView, TransferMoneyView

urlpatterns = [
    path("balance/", TopUpBalanceView.as_view(), name="balance"),
    path("status/", StatusAdminView.as_view(), name="status"),
    path("transfer_money/", TransferMoneyView.as_view(), name="money"),
]
