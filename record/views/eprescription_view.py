from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.views.generic import TemplateView ,CreateView
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
from ..forms import Eprescription
from ..models import Patien,Doctor
from accounts.decorators import doctor_required,patient_required
from django.utils.decorators import method_decorator
from ..forms import EprescriptionCreatFotrm,MedicamentCreationForm
# class RecordView(TemplateView):
#     template_name = 'record.html'
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'patient'
#
#         return super().get_context_data(**kwargs)
user = get_user_model()
@login_required
@doctor_required
@patient_required
def eprescription_view(request):
    template = loader.get_template('eprescription.html')
    return HttpResponse(template.render())

class Eprescription_View(CreateView):
    template_name = 'eprescription.html'
