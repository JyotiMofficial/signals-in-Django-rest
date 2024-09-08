from django.db import models


# Create your models here.
# core/models.py
from django.db import models

class SModel(models.Model):
    name = models.CharField(max_length=100)

class ASModel(models.Model):
    name = models.CharField(max_length=100)

class ThreadModel(models.Model):
    name = models.CharField(max_length=100)

class TransactionModel(models.Model):
    name = models.CharField(max_length=100)
