import django


def setup_django():
    try:
        django.setup()
    except Exception as e:
        print(f"Could not set up Django: {e}")
        raise
