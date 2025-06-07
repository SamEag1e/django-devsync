import os
import sys
from pathlib import Path

import django
from django.core.management import call_command


def setup_django():
    # Try to guess settings module or ask user
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
    if not settings_module:
        settings_module = input(
            "Enter your DJANGO_SETTINGS_MODULE "
            "(e.g. myproject.settings, src.config.settings, etc): "
        ).strip()
        os.environ["DJANGO_SETTINGS_MODULE"] = settings_module

    try:
        django.setup()
    except Exception as e:
        print(f"Could not set up Django: {e}")
        sys.exit(1)


def delete_migrations():
    print("Deleting all migration files...")
    base_path = Path(".")
    for migrations_dir in base_path.rglob("migrations"):
        if "venv" in str(migrations_dir):  # skip venvs
            continue
        for file in migrations_dir.glob("*.py"):
            if file.name != "__init__.py":
                file.unlink()
        for file in migrations_dir.glob("*.pyc"):
            file.unlink()
    print("Migrations deleted.\n")


def reset_sqlite():
    # If using SQLite, just delete the db file
    for file in Path(".").glob("*.sqlite3"):
        print(f"Deleting SQLite DB: {file}")
        file.unlink()
        return True
    return False


def run_sync():
    print("Running makemigrations + migrate...")
    call_command("makemigrations", interactive=False)
    call_command("migrate", interactive=False)
    print("DB schema synced with models.\n")


def main():
    print("🚧 django-devsync — For dev use only!\n")
    setup_django()
    delete_migrations()

    if not reset_sqlite():
        print(
            "SQLite DB not found. If you're using Postgres/MySQL, dropping schema is not implemented yet."
        )
        print("    You may need to manually drop the DB before running this.")

    run_sync()


if __name__ == "__main__":
    main()
