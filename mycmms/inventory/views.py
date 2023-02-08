from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Device
from django.http.response import JsonResponse
# Create your views here.


class InventoryBase(TemplateView):
    template_name = "inventory_base.html"
    
    def list_devices(_request):
        devices = list(Device.objects.values())
        data = {'devices': devices}
        return JsonResponse(data)
        
