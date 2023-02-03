from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class InventoryBase(TemplateView):
    template_name = "inventory_base.html"
