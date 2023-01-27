from django.views.generic import TemplateView
from cmms_app import views

class HomePage(TemplateView):
    template_name = "home.html"

