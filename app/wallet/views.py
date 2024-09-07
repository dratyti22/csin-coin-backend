from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from app.wallet.models import Transaction, CsinCoinModel
from app.wallet.permissions import CreateIsAdminOrRead
from app.wallet.serializers import TransactionSerializer, CsinCoinSerializer

User = get_user_model()


class TopUpBalanceView(APIView):
    permission_classes = [IsAdminUser]

    @transaction.atomic
    def post(self, request):
        pk = request.data.get("id")
        amount = request.data.get("amount")
        message = request.data.get("message")
        user = User.objects.get(id=pk)
        user.balance += amount
        user.save()
        return Response({"success": "Balance replenishment completed", "message": message}, status=status.HTTP_200_OK)


class StatusAdminView(APIView):
    permission_classes = [IsAdminUser]

    @transaction.atomic
    def post(self, request):
        pk = request.data.get("id")
        status_user = request.data.get("status")
        user = User.objects.get(id=pk)
        user.status = status_user
        user.save()
        return Response({"success": "Balance replenishment completed"}, status=status.HTTP_200_OK)


class TransferMoneyView(APIView):
    @transaction.atomic
    def post(self, request):
        sender_id = request.data.get('sender_id')
        receiver_id = request.data.get('receiver_id')
        amount = request.data.get('amount')
        if not [sender_id, receiver_id, amount]:
            return Response({"failed": "Need data"}, status=status.HTTP_401_UNAUTHORIZED)
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)

        if sender.status == "frozen" or receiver.status == "frozen":
            return Response(
                {"failed": "You will be able to trade only after a few days"},
                status=status.HTTP_400_BAD_REQUEST)

        if sender.status == "blocked" or receiver.status == "blocked":
            return Response(
                {"failed": "You are blocked, you cannot do anything, to remove please contact the administration"},
                status=status.HTTP_400_BAD_REQUEST)

        # Проверка баланса отправителя
        if sender.balance < amount:
            return Response({"failed": "Sender has insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)

        # Выполнение транзакции
        sender.balance -= amount
        sender.save()

        receiver.balance += amount
        receiver.save()

        # Создание записи о транзакции
        Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)

        return Response({"success": "Money transferred successfully"}, status=status.HTTP_200_OK)


class GetTransferMoneyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        transactions = Transaction.objects.all().select_related("sender", "receiver")
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class CsinCoinView(ListCreateAPIView):
    queryset = CsinCoinModel.objects.all()
    permission_classes = [CreateIsAdminOrRead]
    serializer_class = CsinCoinSerializer

