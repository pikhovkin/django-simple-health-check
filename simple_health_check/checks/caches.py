from typing import Optional

from django.core.cache import CacheKeyWarning, caches

from . import BaseHealthCheck
from ..exceptions import HealthCheckError


class CacheBackends(BaseHealthCheck):
    def __init__(self, alias: Optional[str] = None):
        super().__init__()
        self.alias = alias

    def check(self):
        if self.alias:
            caches[self.alias]
        try:
            for alias in caches:
                if self.alias and alias != self.alias:
                    continue

                cache = caches[alias]
                cache.set('simple_health_check_test', 'ok', timeout=3)
                if cache.get('simple_health_check_test') != 'ok':
                    raise HealthCheckError('Cache key does not match')
        except CacheKeyWarning as e:
            raise HealthCheckError('Cache key warning')
        except ValueError as e:
            raise HealthCheckError('ValueError')
        except ConnectionError as e:
            raise HealthCheckError('Cache connection error')
