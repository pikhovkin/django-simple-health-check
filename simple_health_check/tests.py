from django.test import TestCase, override_settings
from django.apps import apps


class SimpleTest(TestCase):
    def test_liveness(self):
        apps.get_app_config('simple_health_check').register_checks()

        response = self.client.get('/liveness/')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.content == b'ok')

    def test_readiness(self):
        apps.get_app_config('simple_health_check').register_checks()

        response = self.client.get('/readiness/')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.content == b'ok')

    @override_settings(SIMPLE_HEALTH_CHECKS={'simple_health_check.checks.dummy.DummyFalse': None})
    def test_no_readiness(self):
        apps.get_app_config('simple_health_check').register_checks()

        response = self.client.get('/readiness/')
        self.assertTrue(response.status_code == 500)
        self.assertTrue(response.content == b'down')
