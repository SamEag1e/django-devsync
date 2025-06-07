from pathlib import Path


def delete_migrations():
    print("🔍 Scanning for migration files to delete...")

    root_path = input("Enter project root path [default='.']: ").strip() or "."
    base_path = Path(root_path)

    migration_files = []
    for migrations_dir in base_path.rglob("migrations"):
        if any(
            excluded in str(migrations_dir)
            for excluded in ["venv", "site-packages"]
        ):
            continue

        for file in migrations_dir.glob("*.py"):
            if file.name != "__init__.py":
                migration_files.append(file)
        for file in migrations_dir.glob("*.pyc"):
            migration_files.append(file)

    if not migration_files:
        print("✅ No migration files found.")
        return

    print("\n🚨 The following migration files will be deleted:")
    for file in migration_files:
        print(f"  - {file}")

    confirm = (
        input("Are you sure you want to delete all migrations? [y/n]: ")
        .strip()
        .lower()
    )
    if confirm == "y":
        for file in migration_files:
            file.unlink()
        print("✅ All migration files deleted.")
        return

    print("❌ Operation cancelled.")
