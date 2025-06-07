from django.core.management import call_command


def run_sync():
    print("Running makemigrations + migrate...")
    call_command("makemigrations", interactive=False)
    call_command("migrate", interactive=False)
    print("DB schema synced with models.\n")
