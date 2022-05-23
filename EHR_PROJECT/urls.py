"""EHR_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from accounts.views import patientViews,doctorViews,pharmacistView,laboratoryViews,ehr_home_registration

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('accounts.url')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', ehr_home_registration.SignUpView.as_view(), name='signup'),
    path('accounts/signup/patient/', patientViews.PatientSignUpView.as_view(), name='patientSignup'),
    path('accounts/signup/doctor/', doctorViews.DoctorSignUpView.as_view(), name='doctorSignup'),
    path('accounts/signup/pharmacist/', pharmacistView.PharmacistSignUpView.as_view(), name='pharmacistSignup'),
    path('accounts/signup/laboratory/', laboratoryViews.LaboratorySignUpView.as_view(), name='laboratorySignup'),
    # path('',include('record.url')),
]
