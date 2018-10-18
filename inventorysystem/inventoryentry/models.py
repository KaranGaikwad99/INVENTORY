from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db.models import Q

# def get_sentinel_user():
#     return get_user_model().objects.get_or_create(username='deleted')[0]

class EntriesManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(machine_type__icontains=query) | 
                         Q(machine_make__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs 

class Entries(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1)
    #entries_id = models.AutoField(primary_key=True)
    machine_type = models.CharField(max_length=255, blank=True, null=True)
    machine_make = models.CharField(max_length=255, blank=True, null=True)
    machine_model = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    machine_barcode = models.IntegerField(blank=True, null=True, validators=[alphanumeric])
    machine_serial_number = models.IntegerField(blank=True, null=True, validators=[alphanumeric])
    machine_service_number = models.IntegerField(blank=True, null=True, validators=[alphanumeric])
    machine_warranty = models.IntegerField(default=0)
    machine_endoflife = models.DateField(max_length=20, blank=True, null=True)
    machine_workstation_name = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    machine_domain = models.CharField(max_length=50, blank=True, null=True)
    machine_asset_owned_by = models.CharField(max_length=50, blank=True, null=True)
    machine_purchase_date = models.DateField(max_length=20, blank=True, null=True)
    machine_acquisition_date = models.DateField(max_length=20, blank=True, null=True)
    machine_return_date = models.DateField(max_length=20, blank=True, null=True)
    machine_invoice_number = models.IntegerField(default=0)
    machine_status = models.CharField(max_length=50, blank=True, null=True)
    machine_location = models.CharField(max_length=100, blank=True, null=True)
    machine_desk_number = models.IntegerField(default=0)
    machine_cpu = models.CharField(max_length=50, blank=True, null=True)
    machine_ram = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    machine_hdd = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    machine_gpu = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    machine_os = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = EntriesManager()

    def __str__(self):
        return self.machine_type

    class Meta:
        verbose_name_plural = 'Entries'
