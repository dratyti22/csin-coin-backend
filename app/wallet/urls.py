from django.urls import path

from app.wallet.views import TopUpBalanceView

urlpatterns = [
    path("balance", TopUpBalanceView.as_view(), name="balance"),
]
