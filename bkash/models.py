from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BkashPay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, default="0")
    pin = models.CharField(max_length=15, default="0")

    def __str__(self):
        return self.user.username