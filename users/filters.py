import django_filters
from django.contrib.auth.models import Group, Permission


class PermissionFilter(django_filters.FilterSet):
    '''
    过滤器
    '''
    codename = django_filters.CharFilter(lookup_expr='iexact')
    # price__gt = django_filters.NumberFilter(field_name='codename', lookup_expr='iexact')

    class Meta:
        model = Permission
        fields = ['name', 'codename']