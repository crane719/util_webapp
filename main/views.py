from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class index(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        return super().get(request)
