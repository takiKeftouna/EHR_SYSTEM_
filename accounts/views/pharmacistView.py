from django.shortcuts import render
from django.contrib.auth import login as auth_login , get_user_model
from django.shortcuts import render ,redirect
from django.views.generic import CreateView,TemplateView
# from accounts.decorators import doctor_required
from accounts.forms import PharmacistSignUpForm
from accounts.models import User
user = get_user_model()
class PharmacistSignUpView(CreateView):
    model = user
    form_class = PharmacistSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pharmacist'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request,user)
        return redirect('pharmacist:pharmacist_profile')
class PharmacistProfile(TemplateView):
    template_name = 'pharmacist_profile.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pharmacist'
        return super().get_context_data(**kwargs)
