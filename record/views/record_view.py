import datetime
from time import timezone

from django.shortcuts import redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from accounts.decorators import doctor_required
from ..models import ElRecord,Patien,Doctor
from django.contrib.auth import get_user_model
from accounts.views.doctorViews import search
# class RecordView(TemplateView):
#     template_name = 'record.html'
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'patient'
#         return super().get_context_data(**kwargs)


# @doctor_required
# def record_view(request):
#   template = loader.get_template('record.html')
#   return HttpResponse(template.render())
users = get_user_model()
@doctor_required
def record_view(request,username):
    uid = users.objects.get(username=username)
    record=ElRecord(ER_doctor = request.user,
                    ER_patient=uid,
                    # ER_date_creation= timezone.now(),
    )
    record.save()
    return redirect('patient:patient_profile:records:record_url')
   # template = loader.get_template('record.html')

