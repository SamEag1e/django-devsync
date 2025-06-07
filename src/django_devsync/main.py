import os
import sys

from .core import (
    setup_django,
    check_debug,
    delete_migrations,
    reset_db,
    run_sync,
)
from .args import parse_arguments, describe_plan


def main():
    cwd = os.getcwd()
    if cwd not in sys.path:
        sys.path.insert(0, cwd)

    print(
        "🛑🛑🛑 DON'T USE THIS TOOL ON PRODUCTION 🛑🛑🛑\n"
        "🚧 django-devsync is for development use only!\n"
    )

    args = parse_arguments()
    run_all = not any(vars(args).values())

    describe_plan(args)
    setup_django()
    check_debug()

    if run_all or args.delete_migrations:
        delete_migrations()
    if run_all or args.reset_db:
        reset_db()
    if run_all or args.run_sync:
        run_sync()
