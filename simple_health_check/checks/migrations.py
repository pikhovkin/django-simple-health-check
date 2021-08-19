from typing import Optional

from django.db import DatabaseError, connections
from django.db.migrations.executor import MigrationExecutor

from . import BaseHealthCheck
from ..exceptions import HealthCheckError


class Migrations(BaseHealthCheck):
    def __init__(self, alias: Optional[str] = None):
        super().__init__()
        self.alias = alias

    def check(self):
        if self.alias:
            connections[self.alias]
        try:
            for connection in connections.all():
                if self.alias and connection.alias != self.alias:
                    continue

                executor = MigrationExecutor(connection)
                plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
                if plan:
                    raise HealthCheckError(f'Migrations pending on "{connection.alias}" database')
        except DatabaseError as e:
            raise HealthCheckError('Database is not ready')
        except Exception as e:
            raise HealthCheckError('Unexpected error')
