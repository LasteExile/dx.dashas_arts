from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, FormView, TemplateView
from django.shortcuts import redirect

from . import models, forms

class HomeView(ListView):
    model = models.Drawing
    template_name = 'drawings/home.html'


class MakeAnOrderView(FormView):
    form_class = forms.MakeAnOrderForm
    template_name = 'drawings/makeanorder.html'
    success_url = 'makeanorder/thanks'

    def form_valid(self, form):
        form.send_order(self.request.POST)        
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = 'drawings/thanks.html'


class AboutView(TemplateView):
    template_name = 'drawings/about.html'