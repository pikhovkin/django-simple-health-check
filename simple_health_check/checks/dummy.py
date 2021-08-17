from . import BaseHealthCheck
from ..exceptions import HealthCheckError


class DummyTrue(BaseHealthCheck):
    def check(self):
        ...


class DummyFalse(BaseHealthCheck):
    def check(self):
        raise HealthCheckError('Dummy false')
