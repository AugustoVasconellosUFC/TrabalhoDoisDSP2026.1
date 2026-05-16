from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    senha: str = Field(nullable=False)
    
    enderecos: List["Endereco"] = Relationship(back_populates="usuario")
    pedidos: List["Pedido"] = Relationship(back_populates="usuario")