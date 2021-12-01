from django.conf import settings
from django.core.signals import setting_changed

from .apps import SimpleHealthCheckConfig


ERROR_CODE = getattr(settings, 'SIMPLE_HEALTH_CHECK_ERROR_CODE', 503) or 503


def reload_settings(setting, value, **kwargs):
    if setting == 'SIMPLE_HEALTH_CHECKS':
        SimpleHealthCheckConfig.register_checks()
    elif setting == 'SIMPLE_HEALTH_CHECK_ERROR_CODE':
        global ERROR_CODE
        ERROR_CODE = value


setting_changed.connect(reload_settings)
