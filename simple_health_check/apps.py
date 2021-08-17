from django.apps import AppConfig
from django.conf import settings
from django.utils.module_loading import import_string


class SimpleHealthCheckConfig(AppConfig):
    name = 'simple_health_check'

    checks = {}

    @classmethod
    def register_checks(cls):
        cls.checks = {}
        SIMPLE_HEALTH_CHECKS = getattr(settings, 'SIMPLE_HEALTH_CHECKS', None)
        if SIMPLE_HEALTH_CHECKS is None:
            SIMPLE_HEALTH_CHECKS = {
                'simple_health_check.checks.migrations.Migrations': None,
                'simple_health_check.checks.db.Databases': None,
            }
        for cls_check, options in SIMPLE_HEALTH_CHECKS.items():
            options = options or {}
            if isinstance(options, dict):
                options = [options]
            elif isinstance(options, (list, set, tuple)):
                ...
            else:
                raise
            try:
                Check = import_string(cls_check)
            except Exception:
                raise
            for opt in options:
                identifier = hash(f'{cls_check}.{hash(frozenset((opt or {}).items()))}')
                if identifier in cls.checks:
                    raise
                check = Check(**opt) if opt else Check()
                cls.checks[identifier] = check

    @classmethod
    def check_all(cls):
        for check in cls.checks.values():
            check.check()

    def ready(self):
        self.register_checks()
