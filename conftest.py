# -*- coding: utf-8 -*-
import os
import pytest


def pytest_configure():
    """ pytest setup. """

    import django
    from django.conf import settings

    settings.configure(
        DEBUG=False,
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                               'NAME': ':memory:'}},
        SECRET_KEY='not very secret in tests',
        USE_I18N=True,
        USE_L10N=True,
        STATIC_URL='/static/',
        ROOT_URLCONF='tests.urls',
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ),
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
        ),
    )

    if django.get_version() >= '1.7':
        django.setup()


@pytest.fixture
def pdf_file_sample():
    """ pytest fixture to get sample pdf file and run tests. """

    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'tests',
        'data',
        'sample.pdf'
    )
