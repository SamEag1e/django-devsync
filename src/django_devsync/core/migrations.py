from pathlib import Path


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
