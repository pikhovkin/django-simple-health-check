import locale
import socket

import psutil

from . import BaseHealthCheck
from ..exceptions import HealthCheckError


host = socket.gethostname()


class DiskUsage(BaseHealthCheck):
    def __init__(self, max_usage_percent: int = 0):
        super().__init__()

        self.max_usage_percent = max_usage_percent

    def check(self):
        if not self.max_usage_percent:
            return

        du = psutil.disk_usage('/')
        if du.percent >= self.max_usage_percent:
            raise HealthCheckError(f'{host} {du.percent}% disk usage exceeds {self.max_usage_percent}%')


class MemoryUsage(BaseHealthCheck):
    MB_1 = 1024 * 1024

    def __init__(self, min_memory_mb: int = 0):
        super().__init__()

        self.min_memory_mb = min_memory_mb
        self._min_memory_mb = min_memory_mb * self.MB_1

    def check(self):
        if not self.min_memory_mb:
            return

        memory = psutil.virtual_memory()
        if memory.available < self._min_memory_mb:
            locale.setlocale(locale.LC_ALL, '')
            available = round(memory.available / self.MB_1, 2)
            raise HealthCheckError(f'{host} {available:n} MB available RAM below {self.min_memory_mb:d} MB')
