from django.core.exceptions import PermissionDenied, ValidationError
from pydantic.error_wrappers import ValidationError as PyValidationError
from rest_framework import exceptions as rest_exceptions
from .utils import get_error_message


class ServiceExceptionHandlerMixin:

    expected_exceptions = {
        ValueError: rest_exceptions.ValidationError,
        ValidationError: rest_exceptions.ValidationError,
        PyValidationError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied,
        PermissionDenied: rest_exceptions.PermissionDenied,
    }

    def handle_exception(self, exc):
        if isinstance(exc, tuple(self.expected_exceptions.keys())):
            drf_exception_class = self.expected_exceptions[exc.__class__]
            drf_exception = drf_exception_class(get_error_message(exc))

            return super().handle_exception(drf_exception)

        return super().handle_exception(exc)