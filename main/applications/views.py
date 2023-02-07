from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .common.mixins import ServiceExceptionHandlerMixin
from .common.pagination import get_paginated_response
from rest_framework import serializers
from .models import Application


class ListApplicationsApi(ServiceExceptionHandlerMixin, APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Application

    def get(self, request):
        products = []
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=products,
            request=request,
            view=self,
        )


class CreateApplicationApi(ServiceExceptionHandlerMixin, APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            fields = ["id", "app_type"]
            model = Application

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            fields = "__all__"
            model = Application

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        print(validated_data)
        resp = Application.objects.create(
            id=validated_data["id"]
        )
        return Response(
            self.OutputSerializer(resp).data, status=status.HTTP_201_CREATED
        )
