from .models import Entries
import django_filters
      
class EntriesFilter(django_filters.FilterSet):
    machine_type = django_filters.CharFilter(lookup_expr='icontains')
    machine_make = django_filters.CharFilter(lookup_expr='icontains')
    machine_model = django_filters.CharFilter(lookup_expr='icontains')

    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    class Meta:
        model = Entries
        fields = ['machine_type', 'machine_make', 'machine_model', ]