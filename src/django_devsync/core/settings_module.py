import os
import importlib


def get_settings():
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")

    if settings_module:
        return settings_module

    while True:
        settings_module = input(
            "Enter your DJANGO_SETTINGS_MODULE "
            "(e.g. myproject.settings, src.config.settings, etc): "
        ).strip()

        try:
            importlib.import_module(settings_module)
            return settings_module  # Returns once a valid module is found

        except ModuleNotFoundError:
            print(f"Invalid settings module: '{settings_module}'. Try again.")
