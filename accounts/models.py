from django.db import models
from django.contrib.auth.models import AbstractUser
from EHR_PROJECT import settings

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    is_laboratory = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    specialite = models.CharField(max_length=255,default=False)

class Pharmacist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    adress = models.CharField(max_length=255,default=False)

class Laboratory(models.Model):
    user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    adress = models.CharField(max_length=255 , default=False)

class Patien(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    phone = models.IntegerField(default=False)

