from django.core.management import call_command

from .utils import confirm


def run_sync() -> None:
    print("\nRunning makemigrations + migrate...")
    if not confirm():
        return

    call_command("makemigrations", interactive=False)
    call_command("migrate", interactive=False)
    print("DB schema synced with models.\n")
