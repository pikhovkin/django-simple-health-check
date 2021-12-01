import logging

from django.views import View
from django.http import HttpResponse, HttpResponseServerError

from .apps import SimpleHealthCheckConfig
from . import settings


logger = logging.getLogger(__name__)


class Liveness(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return HttpResponse('ok')


class Readiness(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        try:
            SimpleHealthCheckConfig.check_all()
        except Exception as e:
            logger.exception(e)
            return HttpResponseServerError('down', status=settings.ERROR_CODE)
        return HttpResponse('ok')
