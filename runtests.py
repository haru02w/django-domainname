#!/usr/bin/env python
from django.test.utils import get_runner
import sys

import django
from django.conf import settings


SETTINGS = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    'INSTALLED_APPS': (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.admin',
        'django_dnf.tests',
        'django_dnf',
    ),
    'SITE_ID': 1,
    'SECRET_KEY': 'test',
    'TEMPLATES': [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ]
            }
        }
    ],
}

if django.VERSION < (2, 2):
    SETTINGS['MIDDLEWARE_CLASSES'] = (
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
    )
else:
    SETTINGS['MIDDLEWARE'] = (
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
    )


if not settings.configured:
    settings.configure(**SETTINGS)


def runtests():
    if hasattr(django, 'setup'):
        django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    apps = ['django_dnf', ]
    failures = test_runner.run_tests(apps)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
