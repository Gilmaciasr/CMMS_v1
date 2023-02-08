from django.db import models

# Create your models here.
class Device(models.Model):
    """Model definition for Device."""
    inventory_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    dmodel = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    last_pm = models.DateField()
    next_pm = models.DateField()
    install_date = models.DateField()
    history = models.CharField(max_length=200)
    
    class Meta:
        """Meta definition for Device."""
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

