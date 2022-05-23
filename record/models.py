from django.db import models
from accounts.models import Doctor,Patien,Pharmacist,Laboratory
from django.contrib.auth import get_user_model

# Create your models here.
class ElRecord(models.Model):
    ER_doctor=models.ForeignKey(get_user_model(),default=False,on_delete=models.CASCADE)
    ER_patient = models.ForeignKey(get_user_model(),default=False,related_name='patient',on_delete=models.CASCADE)
    # ER_date_creation = models.DateTimeField(default=True)
class ReportMedicale(models.Model):
    pass
class Eprescription(models.Model):
    record = models.ForeignKey(ElRecord,default=False,on_delete=models.CASCADE)
    created_By = models.OneToOneField(get_user_model(),default=True,on_delete=models.CASCADE)

class Medicament(models.Model):
    Epres = models.ForeignKey(Eprescription,on_delete=models.CASCADE)
    medicament=models.CharField(max_length=255)
    description=models.TextField(max_length=400)
class CerteficateMedicake(models.Model):
    pass
class Analyses(models.Model):
    pass
class ResultOfAnalyses(models.Model):
    pass