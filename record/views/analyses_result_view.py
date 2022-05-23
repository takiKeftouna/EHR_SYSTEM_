from django.shortcuts import redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

# class RecordView(TemplateView):
#     template_name = 'record.html'
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'patient'
#         return super().get_context_data(**kwargs)
def analyses_result_view(request):
  template = loader.get_template('analyses.html')
  return HttpResponse(template.render())