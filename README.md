# django-devsync

A tiny, dangerous Django utility for dev-mode schema syncing — wipe all migrations, rebuild from models, and auto-apply. Use only in development.

- Splitting stuff into other reusable modules, so that I'll be able to split cli commands
- Adding some safety checks and warnings before doing dangerous things such as removing migrations or tables etc
- Adding remove of tables for MySQL and PostgreSQL
- Having soft_delete option( which will create a backup folder in the root of user's project and moves migration files there with a backup of db )
- Will check DEBUG = TRUE and give warning that if your debug is false your're probably in production and IT's not SAFE to use this and so on.
