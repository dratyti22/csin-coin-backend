from django.urls import path

from app.wallet.views import TopUpBalanceView, StatusAdminView, TransferMoneyView, GetTransferMoneyView, CsinCoinView

urlpatterns = [
    path("balance/", TopUpBalanceView.as_view(), name="balance"),
    path("status/", StatusAdminView.as_view(), name="status"),
    path("transfer_money/", TransferMoneyView.as_view(), name="money"),
    path("get_transfer/", GetTransferMoneyView.as_view(), name="transfer"),
    path("coin/", CsinCoinView.as_view(), name="coin"),
]
