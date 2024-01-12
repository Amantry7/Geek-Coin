from django.urls import path


from .views import UserAPI, TransactionAPI, PayrollCoins, BurnCoin, TransferCoin

urlpatterns = [
    path('users/', UserAPI.as_view(), name='api_user'),
    path('transactions/', TransactionAPI.as_view(), name='api_transaction'),
    path('payroll-coins/<str:user>/', PayrollCoins.as_view(), name='payroll-coins'),
    path('burn-coins/', BurnCoin.as_view(), name='burn-coins'),
    path('transfer-coins/<str:sender_user>/<str:receiver_user>/', TransferCoin.as_view(), name='transfer-coins'),
]
