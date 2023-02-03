from django.urls import path
from . import views

app_name = "metrics"

urlpatterns = [
    path('metrics/', views.MetricsBase.as_view(template_name='metrics/metrics_base.html'), name='metrics'),
    
]