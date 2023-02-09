from django_filters.rest_framework import FilterSet, CharFilter, ChoiceFilter
from .models import Application
from .common.entities import Status, ProblemType


class ApplicationFilter(FilterSet):
    user_id = CharFilter(
        field_name="user_id",
    )
    app_type = ChoiceFilter(
        choices=ProblemType.choices,
        field_name="app_type"
    )
    app_status = ChoiceFilter(
        choices=Status.choices,
        field_name="app_status"
    )
    address = CharFilter(
        field_name="address",
        lookup_expr="contains",
    )

    class Meta:
        model = Application
        fields = "__all__"
