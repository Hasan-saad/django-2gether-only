import django_filters
from .models import ServicProvider

class ServicProviderFilter(django_filters.FilterSet):
    # fName = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ServicProvider
        fields = '__all__'
        exclude = ['user', 'img', 'fName', 'lName', 'publishAt', 'Vacancy']