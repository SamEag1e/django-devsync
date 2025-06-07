from .core import (
    get_settings,
    setup_django,
    delete_migrations,
    reset_db,
    run_sync,
)


def main():
    print("🚧 django-devsync — For dev use only!\n")

    settings = get_settings()
    setup_django()
    delete_migrations()
    reset_db(settings)
    run_sync()


if __name__ == "__main__":
    main()
