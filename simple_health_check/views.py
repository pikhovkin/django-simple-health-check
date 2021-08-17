import logging

from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseServerError

from .apps import SimpleHealthCheckConfig


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
            logger.error(e)
            return HttpResponseServerError('down')
        return HttpResponse('ok')
