from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm

from .models import Medicament,Eprescription,Analyses,ResultOfAnalyses,ReportMedicale,CerteficateMedicake
from django.contrib.auth import get_user_model

class EprescriptionCreatFotrm(ModelForm):
    class Meta:
        model=Eprescription
        fields = '__all__'
class MedicamentCreationForm(ModelForm):
    class Meta:
        medel = Medicament
        fields = '__all__'
