import os
import sys


current_dir = os.path.dirname(os.path.realpath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))


sys.path.append(parent_dir)


from datebase.database import db
from datebase.Modules import User, Game

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context


from app import app  

target_metadata = db.metadata

config = context.config
config.set_main_option("sqlalchemy.url", app.config["SQLALCHEMY_DATABASE_URI"])
fileConfig(config.config_file_name)


# with app.app_context():
#     connectable = db.engine
#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection,
#             target_metadata=db.metadata,
#             compare_type=True,
#             compare_server_default=True,
#         )

#         with context.begin_transaction():
#             context.run_migrations()


def run_migrations_online():
    
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()