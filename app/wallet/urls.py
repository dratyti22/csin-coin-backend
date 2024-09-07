from django.urls import path

from app.wallet.views import TopUpBalanceView, StatusAdminView

urlpatterns = [
    path("balance/", TopUpBalanceView.as_view(), name="balance"),
    path("status/", StatusAdminView.as_view(), name="status"),
]
