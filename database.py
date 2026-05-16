"""
JUSTIFICATIVA DA ALTERAÇÃO: Gerencia a conexão assíncrona exigida (AsyncEngine e AsyncSession),
com correção na tipagem do AsyncIterator para evitar falhas de execução e um
fallback de segurança caso ocorram problemas na leitura do arquivo .env.
"""
import os
import logging
from collections.abc import AsyncIterator
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurar logging para visualizar as queries SQL no console
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Busca a URL do banco. Se o .env falhar, cai com segurança no SQLite local.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///exemplo-orm.db")

# Configuração do motor assíncrono
engine = create_async_engine(DATABASE_URL)

# Gerador de sessões assíncronas
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session