from django.forms import ModelForm
from django import forms
from .models import Entries
from django.forms import widgets
from django_popup_view_field.fields import PopupViewField

class EntriesForm(ModelForm):
    
    class Meta:
        model = Entries
        
        fields = ['machine_type', 'machine_make', 'machine_model', 'machine_barcode', 
        'machine_serial_number', 'machine_service_number', 'machine_warranty', 'machine_endoflife', 'machine_workstation_name',
        'machine_domain', 'machine_asset_owned_by', 'machine_purchase_date', 'machine_acquisition_date', 'machine_return_date', 
        'machine_invoice_number', 'machine_status', 'machine_location', 'machine_desk_number', 'machine_cpu', 'machine_ram', 'machine_hdd',
        'machine_gpu', 'machine_os']

        labels = {
            'machine_type':'Type', 
            'machine_make':'Make', 
            'machine_model':'Model', 
            'machine_barcode':'Barcode', 
            'machine_serial_number':'Serial Number', 
            'machine_service_number':'Service Number', 
            'machine_warranty':'Warrenty', 
            'machine_endoflife':'End Of Life', 
            'machine_workstation_name':'Work Station Name',
            'machine_domain':'Domain', 
            'machine_asset_owned_by' : 'Asset Own By', 
            'machine_purchase_date' : 'Purchase Date', 
            'machine_acquisition_date' : 'Acquistion Date', 
            'machine_return_date' : 'Return Date', 
            'machine_invoice_number' : 'Invoice Number', 
            'machine_status' : 'Status', 
            'machine_location' : 'Location', 
            'machine_desk_number' : 'Desk Number', 
            'machine_cpu' : 'CPU', 
            'machine_ram' : 'RAM', 
            'machine_hdd' : 'HDD',
            'machine_gpu': 'GPU', 
            'machine_os':'OS',
       }
