from import_export import resources
from .models import Entries

class EntriesResource(resources.ModelResource):
    class Meta:
        model = Entries

