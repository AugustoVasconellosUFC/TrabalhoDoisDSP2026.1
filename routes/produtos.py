from fastapi import APIRouter, HTTPException, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlmodel import apaginate
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from models import produto #WIP
from database import get_session
from datetime import datetime, timezone

router = APIRouter(
    prefix="/produtos",  # Prefixo para todas as rotas
    tags=["Produtos"],   # Tag para documentação automática
)