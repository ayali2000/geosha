from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Quest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None, null=True, blank=True)
    question = models.CharField(max_length=1000)
    date_ask = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_ask']

class Ans(models.Model):
    quest = models.ForeignKey(Quest,on_delete=models.CASCADE, default=None, null=True, blank=True,related_name='ans')
    ans = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_ans = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ans']

