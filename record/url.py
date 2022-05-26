
from .views import analyses_result_view,certeficate_view,analyses_view,record_view,eprescription_view,report_medicale_view
from django.urls import path,include
urlpatterns = [
path('records/', include(([
       path('record',record_view.record_view,name='record_url'),
       path('eprescription',eprescription_view.eprescription_view,name='eprescription_url'),
       path('medicalereport',report_medicale_view.medicale_report_view,name='medicale_report_url'),
       path('medicalecerteficate',certeficate_view.medicale_certeficate_view,name='medicale_certeficate_url'),
       path('requiredanalyses',analyses_view.required_analyses_view,name='required_analeses_url'),
       path('requiredanalyses', analyses_result_view.analyses_result_view,name='analyses_result_url'),
 ], 'record'), namespace='records')),
]