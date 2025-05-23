from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    creator = filters.NumberFilter(field_name='creator', lookup_expr='exact')

    created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at_before']
