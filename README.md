# django-simple-health-check

[![GitHub Actions](https://github.com/pikhovkin/django-simple-health-check/workflows/build/badge.svg)](https://github.com/pikhovkin/django-simple-health-check/actions)
[![PyPI](https://img.shields.io/pypi/v/django-simple-health-check.svg)](https://pypi.org/project/django-simple-health-check/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-simple-health-check.svg)
[![framework - Django](https://img.shields.io/badge/framework-Django-0C3C26.svg)](https://www.djangoproject.com/)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-simple-health-check.svg)
[![PyPI - License](https://img.shields.io/pypi/l/django-simple-health-check)](./LICENSE)

Simple Django health check

Inspired by:
- [django-alive](https://github.com/lincolnloop/django-alive)
- [django-healthchecks](https://github.com/mvantellingen/django-healthchecks)
- [django-health-check](https://github.com/KristianOellegaard/django-health-check)
- [django-healthz](https://github.com/rehive/django-healthz)
- [django-watchman](https://github.com/mwarkentin/django-watchman)

### Installation

```bash
$ pip install django-simple-health-check
```

### Quick start

1. Install the package

2. Add `simple_health_check` to your INSTALLED_APPS settings like this:

```python
INSTALLED_APPS = [
    ...,
    'simple_health_check',
    ...,
]
```

3. Add `simple_health_check.urls` to main `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...,
    path('', include('simple_health_check.urls')),
    ...,
]
```

4. Configure the readiness checks:

```python
SIMPLE_HEALTH_CHECKS = {
    'simple_health_check.checks.migrations.Migrations': [
        dict(alias='db1'),
        dict(alias='db2'),
    ],
    'simple_health_check.checks.db.Databases': None,

    # The simplest way to add your own check 
    'your_package.path_to_checks.SomeCheck': {...} or [{...}, ...] or None,  
}
```

by default

```python
SIMPLE_HEALTH_CHECKS = {
    'simple_health_check.checks.migrations.Migrations': None,  # check all aliases
    'simple_health_check.checks.db.Databases': None,  # check all aliases
}
```

### Built-in checks

| A check                                          |     Built-in/expected    |
|--------------------------------------------------|:------------------------:|
| simple_health_check.checks.db.Databases          |    :heavy_check_mark:    |
| simple_health_check.checks.migrations.Migrations |    :heavy_check_mark:    |
| simple_health_check.checks.caches.CacheBackends  |    :heavy_check_mark:    |
| simple_health_check.checks.ps.DiskUsage          |    :heavy_check_mark:    |
| simple_health_check.checks.ps.MemoryUsage        |    :heavy_check_mark:    |
| simple_health_check.checks.dummy.DummyTrue       |    :heavy_check_mark:    |
| simple_health_check.checks.dummy.DummyFalse      |    :heavy_check_mark:    |
| emails                                           | :hourglass_flowing_sand: |
| queues                                           | :hourglass_flowing_sand: |
| storages                                         | :hourglass_flowing_sand: |

## License

MIT
