import argparse
from .core import (
    get_settings,
    setup_django,
    delete_migrations,
    reset_db,
    run_sync,
)


def main():
    print("🚧 django-devsync — For dev use only!\n")

    parser = argparse.ArgumentParser(
        description="Sync your dev DB schema like TypeORM synchronize."
    )
    parser.add_argument(
        "--delete_migrations",
        action="store_true",
        help="Delete all migration files",
    )
    parser.add_argument(
        "--reset_db", action="store_true", help="Drop all DB tables/schemas"
    )
    parser.add_argument(
        "--run_sync",
        action="store_true",
        help="Run makemigrations and migrate",
    )

    args = parser.parse_args()

    # If no flags are passed, run all
    run_all = not any(vars(args).values())

    settings = get_settings()
    setup_django()

    if run_all or args.delete_migrations:
        delete_migrations()
    if run_all or args.reset_db:
        reset_db(settings)
    if run_all or args.run_sync:
        run_sync()
