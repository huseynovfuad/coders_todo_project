import django_filters
from django.db.models import Q
from todoapp.models import Todo


class TodoFilter(django_filters.FilterSet):    
    search = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    status = django_filters.BooleanFilter()
    start_date = django_filters.DateFilter(field_name="deadline", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="deadline", lookup_expr="lt")

    class Meta:
        model = Todo
        fields = (
            "search", "status", "start_date", "end_date"
            )