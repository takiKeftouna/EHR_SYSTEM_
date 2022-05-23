from django.shortcuts import render
from django.contrib.auth import login as auth_login , get_user_model
from django.shortcuts import render ,redirect
from django.views.generic import CreateView ,TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import patient_required,doctor_required
from accounts.forms import PatientSignUpForm
from django.http import HttpResponse
from django.contrib.auth import get_user_model
user = get_user_model()
class PatientSignUpView(CreateView):
    model = user
    form_class = PatientSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request,user)
        return redirect('patient:patient_profile')
@method_decorator([login_required,patient_required], name='dispatch')
class PatientProfileView(TemplateView):
    template_name = 'patient_profile.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

