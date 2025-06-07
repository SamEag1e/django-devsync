import os
import importlib

import django


def setup_django():
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")

    if not settings_module:
        while True:
            settings_module = input(
                "Enter your DJANGO_SETTINGS_MODULE "
                "(e.g. myproject.settings, src.config.settings, etc): "
            ).strip()

            try:
                importlib.import_module(settings_module)
                os.environ["DJANGO_SETTINGS_MODULE"] = settings_module
                break

            except ModuleNotFoundError:
                print(
                    f"Invalid settings module: '{settings_module}'. Try again."
                )

    try:
        django.setup()
    except Exception as e:
        print(f"Could not set up Django: {e}")
        raise
