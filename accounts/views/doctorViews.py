from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.shortcuts import render ,redirect
from django.views.generic import CreateView,TemplateView,ListView
from accounts.decorators import doctor_required
from accounts.forms import DoctorSignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import doctor_required
patient_username = 0
user = get_user_model()
class DoctorSignUpView(CreateView):
    model = user
    form_class = DoctorSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request,user)
        return redirect('doctor:doctor_profile')
@method_decorator([login_required, doctor_required], name='dispatch')
class DoctorProfileView(TemplateView):
    template_name = 'doctor_profile.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)
# class PatientS(ListView):
#     model = user
#     template_name = 'doctor_profile.html'
#     queryset = user.objects.filter(username__icontains='taki')
#     def get_queryset(self):  # new
#         query = self.request.GET.get("q")
#         patient = user.objects.filter(username__icontains=query )
#         return patient

def search(request):
    patient = []
    if request.method == "GET":
        if request.GET.get('search'):
            query = request.GET.get('search')
            if query == '':
               query = 'None'
            patient = user.objects.get(username=query)
            print(patient)
    return render(request, 'doctor_profile.html',{'patient':patient},{'query':query})

