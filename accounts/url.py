from django.urls import path , include
from django.contrib.auth import views as auth_views
from accounts.views import doctorViews,patientViews,pharmacistView,laboratoryViews,ehr_home_registration
import record
urlpatterns = [
    path('',ehr_home_registration.home, name='home'),
    path('patient/', include(([
        path('patient_profile/<str:username>/', patientViews.patientProfileView,name='patient_profile'),
        path('patient_profile/',include((('record.url'),'accounts'),namespace='patient_profile'))
        # path('', include(('home.urls', 'home'), namespace='home'))
    ], 'accounts'), namespace='patient')),

    path('doctor/', include(([
        path('doctor_profile/', doctorViews.DoctorProfileView.as_view(), name='doctor_profile'),
    ], 'accounts'), namespace='doctor')),

    path('pharmacist/', include(([
        path('pharmacist_profile/', pharmacistView.PharmacistProfile.as_view(), name='pharmacist_profile'),
    ], 'accounts'), namespace='pharmacist')),

    path('laboratory/', include(([
         path('laboratory_profile/', laboratoryViews.LaboratoryProfileView.as_view(), name='laboratory_profile'),
    ], 'accounts'), namespace='laboratory'))
]

