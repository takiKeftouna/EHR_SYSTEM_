from django.shortcuts import redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

# class RecordView(TemplateView):
#     template_name = 'record.html'
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'patient'
#         return super().get_context_data(**kwargs)
def medicale_report_view(request):
  template = loader.get_template('report_medicale.html')
  return HttpResponse(template.render())