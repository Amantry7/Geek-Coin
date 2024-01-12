from rest_framework import serializers

from .models import User, Transaction

class UserSerializers(serializers. ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class TransactionSerializers(serializers. ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'