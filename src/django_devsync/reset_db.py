import os

from django.conf import settings
from django.db import connection


def reset_db():
    engine = settings.DATABASES["default"]["ENGINE"]

    if "sqlite" in engine:
        db_path = settings.DATABASES["default"]["NAME"]
        if os.path.isfile(db_path):
            os.remove(db_path)
            print(f"Deleted SQLite DB file at: {db_path}")
        else:
            print("No SQLite DB file found to delete.")

    elif "postgresql" in engine:
        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")
        print("Dropped and recreated public schema in PostgreSQL")

    elif "mysql" in engine:
        with connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("SHOW TABLES;")
            tables = [row[0] for row in cursor.fetchall()]
            for table in tables:
                cursor.execute(f"DROP TABLE IF EXISTS `{table}`;")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
        print("Dropped all tables in MySQL")

    else:
        raise NotImplementedError(
            f"DB engine '{engine}' not supported for reset."
        )
