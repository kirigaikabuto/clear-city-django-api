from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .common.mixins import ServiceExceptionHandlerMixin
from .common.pagination import get_paginated_response
from rest_framework import serializers
from .models import Application
from .filters import ApplicationFilter
from .common.entities import Status, ProblemType
from django.shortcuts import get_object_or_404


class ListApplicationsApi(ServiceExceptionHandlerMixin, APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class InputSerializer(serializers.Serializer):
        user_id = serializers.CharField(required=False)
        app_type = serializers.ChoiceField(choices=ProblemType.choices, required=False)
        app_status = serializers.ChoiceField(choices=Status.choices, required=False)
        address = serializers.CharField(required=False)
        id = serializers.CharField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        longitude = serializers.FloatField()
        latitude = serializers.FloatField()

        class Meta:
            fields = "__all__"
            model = Application

    def get(self, request):
        apps = Application.objects.all()
        filters = self.InputSerializer(
            data=request.query_params, context={"request": request}
        )
        filters.is_valid(raise_exception=True)
        print(filters)
        filters = filters.validated_data
        if "id" in filters:
            current_app = get_object_or_404(Application, id=filters["id"])
            return Response(
                self.OutputSerializer(current_app).data, status=status.HTTP_201_CREATED
            )
        result = (
            ApplicationFilter(filters, apps)
            .qs.distinct()
        )
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=result,
            request=request,
            view=self,
        )


class CreateApplicationApi(ServiceExceptionHandlerMixin, APIView):
    class InputSerializer(serializers.ModelSerializer):
        patronymic = serializers.CharField(required=False, allow_null=True, allow_blank=True)
        video_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        app_type = serializers.ChoiceField(choices=ProblemType.choices, required=False)
        app_status = serializers.ChoiceField(choices=Status.choices, required=False)
        first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        photo_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        user_id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        message = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        longitude = serializers.DecimalField(decimal_places=8, max_digits=100, required=False)
        latitude = serializers.DecimalField(decimal_places=8, max_digits=100, required=False)

        class Meta:
            fields = [
                "id",
                "app_type",
                "app_status",
                "message",
                "first_name",
                "last_name",
                "patronymic",
                "phone_number",
                "photo_url",
                "video_url",
                "address",
                "longitude",
                "latitude",
                "user_id",
                "created_date",
            ]
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
            **validated_data
        )
        return Response(
            self.OutputSerializer(resp).data, status=status.HTTP_201_CREATED
        )


class UpdateApplicationApi(ServiceExceptionHandlerMixin, APIView):
    class QuerySerializer(serializers.Serializer):
        id = serializers.CharField()

    class InputSerializer(serializers.ModelSerializer):
        patronymic = serializers.CharField(required=False, allow_null=True, allow_blank=True)
        video_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        app_type = serializers.ChoiceField(choices=ProblemType.choices, required=False)
        app_status = serializers.ChoiceField(choices=Status.choices, required=False)
        first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        photo_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        user_id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        message = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        longitude = serializers.DecimalField(decimal_places=8, max_digits=100, required=False)
        latitude = serializers.DecimalField(decimal_places=8, max_digits=100, required=False)

        class Meta:
            fields = [
                "app_type",
                "app_status",
                "message",
                "first_name",
                "last_name",
                "patronymic",
                "phone_number",
                "photo_url",
                "video_url",
                "address",
                "longitude",
                "latitude",
                "user_id",
                "created_date",
            ]
            model = Application

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            fields = "__all__"
            model = Application

    def put(self, request):
        filters = self.QuerySerializer(
            data=request.query_params, context={"request": request}
        )
        filters.is_valid(raise_exception=True)
        filters = filters.validated_data
        serializer = self.InputSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        app = get_object_or_404(Application, id=filters["id"])
        updated_fields = []
        if "first_name" in validated_data:
            app.first_name = validated_data.get("first_name")
            updated_fields.append("first_name")
        if "last_name" in validated_data:
            app.last_name = validated_data.get("last_name")
            updated_fields.append("last_name")
        if "app_type" in validated_data:
            app.app_type = validated_data.get("app_type")
            updated_fields.append("app_type")
        if "app_status" in validated_data:
            app.app_status = validated_data.get("app_status")
            updated_fields.append("app_status")
        if "message" in validated_data:
            app.message = validated_data.get("message")
            updated_fields.append("message")
        if "patronymic" in validated_data:
            app.patronymic = validated_data.get("patronymic")
            updated_fields.append("patronymic")
        if "photo_url" in validated_data:
            app.photo_url = validated_data.get("photo_url")
            updated_fields.append("photo_url")
        if "video_url" in validated_data:
            app.video_url = validated_data.get("video_url")
            updated_fields.append("video_url")
        if "address" in validated_data:
            app.video_url = validated_data.get("address")
            updated_fields.append("address")
        if "address" in validated_data:
            app.video_url = validated_data.get("address")
            updated_fields.append("address")
        if "longitude" in validated_data:
            app.longitude = validated_data.get("longitude")
            updated_fields.append("longitude")
        if "latitude" in validated_data:
            app.latitude = validated_data.get("latitude")
            updated_fields.append("latitude")
        if "user_id" in validated_data:
            app.user_id = validated_data.get("user_id")
            updated_fields.append("user_id")

        if len(updated_fields) != 0:
            app.save()
        return Response(
            self.OutputSerializer(app).data, status=status.HTTP_200_OK
        )


class DeleteApplicationApi(ServiceExceptionHandlerMixin, APIView):
    class QuerySerializer(serializers.Serializer):
        id = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            fields = "__all__"
            model = Application

    def delete(self, request):
        filters = self.QuerySerializer(
            data=request.query_params, context={"request": request}
        )
        filters.is_valid(raise_exception=True)
        filters = filters.validated_data
        app = get_object_or_404(Application, id=filters["id"])
        app.delete()
        return Response(
            self.OutputSerializer(app).data, status=status.HTTP_200_OK
        )
