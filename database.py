from collections.abc import AsyncIterator
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging
import os

# Carregar variávies do arquivo .env
load_dotenv()

# Configurar logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Configuração do banco de dados
engine = create_async_engine(os.getenv("DATABASE_URL"))

# Gerador de sessões assíncronas
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncIterator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session