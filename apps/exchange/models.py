from django.db import models

class User(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя студента'
    )
    direction = models.CharField(
        max_length=255,
        verbose_name='Направление'
    )
    mount = models.CharField(
        max_length=255,
        verbose_name='Месяц'
    )
    geek_coins_balance = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.direction} - {self.mount}'

class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions')
    coin = models.IntegerField()
    transaction_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.name} to {self.recipient.name}, Amount: {self.coin}, Time: {self.timestamp}"
