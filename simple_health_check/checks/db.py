from typing import Optional

from django.db import DatabaseError, connections

from . import BaseHealthCheck
from ..exceptions import HealthCheckError


class Databases(BaseHealthCheck):
    def __init__(self, query: str = 'SELECT 1; -- simple_health_check', alias: Optional[str] = None):
        super().__init__()
        self.query = query
        self.alias = alias

    def check(self):
        if self.alias:
            connections[self.alias]
        try:
            for connection in connections.all():
                if self.alias and connection.alias != self.alias:
                    continue

                with connection.cursor() as cursor:
                    cursor.execute(self.query)
                    row = cursor.fetchone()
                    if row is None:
                        raise HealthCheckError(f'"{connection.alias}" database connection failed')
        except DatabaseError as e:
            raise HealthCheckError('Database is not ready')
        except Exception as e:
            raise HealthCheckError('Unexpected error')
