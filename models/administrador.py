from typing import Optional
from sqlmodel import SQLModel, Field

class Administrador(SQLModel, table=True):
    __tablename__ = "administrador"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    senha: str = Field(nullable=False)