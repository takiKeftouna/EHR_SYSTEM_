from django.shortcuts import redirect,render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctor:doctor_profile')
        elif request.user.is_pharmacist:
            return redirect('pharmacist:pharmacist_profile')
        elif request.user.is_laboratory:
            return redirect('laboratory:laboratory_profile')
        elif request.user.is_patient:
            return redirect('patient:patient_profile')
    return render(request,'home.html')
