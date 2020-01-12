from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from . import forms

# Create your views here.
class index(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        return super().get(request)


class MultiUploadView(FormView):
    form_class = forms.MultipleUploadForm
    template_name = 'main/upload.html'

    def form_valid(self, form):
        download_url_list = form.save()
        context = {
            'download_url_list': download_url_list,
            'form': form,
        }
        return self.render_to_response(context)

