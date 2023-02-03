from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path('inventory/', views.InventoryBase.as_view(template_name='inventory/inventory_base.html'), name='inventory'),
    
]