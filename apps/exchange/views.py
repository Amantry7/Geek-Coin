from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Transaction
from .serializers import UserSerializers, TransactionSerializers

# Create your views here.

class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
class TransactionAPI(ListAPIView, CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class=TransactionSerializers
    
class PayrollCoins(APIView):
    def post(self, request, user):
        try:
            user = User.objects.get(name=user)
        except User.DoesNotExist:
            return Response({'error': 'User не найден'}, status=status.HTTP_404_NOT_FOUND)

        user.geek_coins_balance += 4
        user.save()

        transaction = Transaction.objects.create(sender=user, coin=4, transaction_type='payroll')

        return Response({'message': 'Coins credited successfully'}, status=status.HTTP_200_OK)



class BurnCoin(APIView):
    def post(self, request):
        Transaction.objects.filter(coin__gt=0).update(transaction_type='burn')
        User.objects.filter(geek_coins_balance__gt=0).update(geek_coins_balance=0)

        return Response({'message': "Коины сгорели"}, status=status.HTTP_200_OK)

    
    
class TransferCoin(APIView):
    def post(self, request, sender_user, receiver_user):
        try:
            sender = User.objects.get(name=sender_user)
            receiver = User.objects.get(name=receiver_user)
        except User.DoesNotExist:
            return Response({'error': 'Ученик не найден'}, status=status.HTTP_404_NOT_FOUND)

        if sender.geek_coins_balance < 1:
            return Response({'error': 'Недостаточно гик коинов'}, status=status.HTTP_400_BAD_REQUEST)

        sender.geek_coins_balance -= 1
        receiver.geek_coins_balance += 1
        sender.save()
        receiver.save()

        # Используйте поля модели Transaction для создания объекта
        Transaction.objects.create(sender=sender, recipient=receiver, coin=1)

        return Response({'message': 'Вы успешно передали geek coin'}, status=status.HTTP_200_OK)
