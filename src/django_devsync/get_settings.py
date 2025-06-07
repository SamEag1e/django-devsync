import os


def get_settings():
    # Try to guess settings module or ask user
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
    if not settings_module:
        # Ask for entering settings module,
        # and check if it exists and it's the right one for django project
        # if not, ask again (in a loop)
        settings_module = input(
            "Enter your DJANGO_SETTINGS_MODULE "
            "(e.g. myproject.settings, src.config.settings, etc): "
        ).strip()

    return settings_module
