from django.shortcuts import render
from django.contrib.auth import login as auth_login , get_user_model
from django.shortcuts import render ,redirect
from django.views.generic import CreateView ,TemplateView

# from accounts.decorators import doctor_required
from accounts.forms import LaboratorySignUpForm

user = get_user_model()
class LaboratorySignUpView(CreateView):
    model = user
    form_class = LaboratorySignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'laboratory'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request,user)
        return redirect('laboratory:laboratory_profile')
class LaboratoryProfileView(TemplateView):
    template_name = 'laboratory_profile.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'laboratory'
        return super().get_context_data(**kwargs)