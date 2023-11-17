#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-simple-health-check',
    version='0.6.0',
    description='Simple Django health check',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sergei Pikhovkin',
    author_email='s@pikhovkin.ru',
    url='https://github.com/pikhovkin/django-simple-health-check',
    packages=[
        'simple_health_check',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=3.1,<5.1',
    ],
    extras_require={
        'psutil': ['psutil'],
    },
    python_requires='>=3.7,<4.0',
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords=[
        'django', 'monitoring', 'healthcheck', 'health-check', 'ping', 'health-checks', 'healthchecks',
        'liveness', 'readiness', 'liveness-detection', 'readiness-checker', 'django-health-check',
        'readiness-detection', 'liveness-checker',
    ],
)
