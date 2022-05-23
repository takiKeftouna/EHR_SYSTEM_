from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Doctor,Patien,Pharmacist,Laboratory,User
from django.contrib.auth import get_user_model

#doctor signUp forms
user = get_user_model()
class DoctorSignUpForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
         model = user
     @transaction.atomic
     def save(self):
         user = super().save(commit=False)
         user.is_doctor = True
         user.save()
         doctor = Doctor(user=user)
         doctor.save()
         return user

# patient sign Up forms
class PatientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = user
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patien(user=user)
        patient.save()
        return user

class PharmacistSignUpForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
         model = user
     @transaction.atomic
     def save(self):
         user = super().save(commit=False)
         user.is_pharmacist = True
         user.save()
         pharmacist = Pharmacist(user=user)
         pharmacist.save()
         return user

class LaboratorySignUpForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
         model = user
     @transaction.atomic
     def save(self):
         user = super().save(commit=False)
         user.is_laboratory = True
         user.save()
         laboratory = Laboratory(user=user)
         laboratory.save()
         return user
