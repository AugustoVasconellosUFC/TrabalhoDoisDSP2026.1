import asyncio
import os
from logging.config import fileConfig
from dotenv import load_dotenv

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context

# Importa o SQLModel e força a descoberta das tabelas registradas no __init__
from sqlmodel import SQLModel
import models

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Objeto de configuração do Alembic
config = context.config

# Injeta a URL do banco do .env diretamente na configuração do Alembic
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configura os logs se o arquivo de configuração existir
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define o metadata do SQLModel para que o Alembic saiba quais tabelas criar
target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    """Executa as migrações no modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Executa as migrações no modo 'online' (assíncrono)."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())