from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from datebase.database import db
from alembic import context

from datebase.Modules import User  

from app import app  

config = context.config
config.set_main_option("sqlalchemy.url", app.config["SQLALCHEMY_DATABASE_URI"])
fileConfig(config.config_file_name)

# Run migrations in 'online' mode
with app.app_context():
    connectable = db.engine
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=db.metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()
