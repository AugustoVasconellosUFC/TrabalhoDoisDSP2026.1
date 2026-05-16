from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Endereco(SQLModel, table=True):
    __tablename__ = "endereco"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    rua: str = Field(nullable=False)
    cidade: str = Field(nullable=False)
    estado: str = Field(nullable=False)
    cep: str = Field(nullable=False)
    
    usuario_id: int = Field(foreign_key="usuario.id", nullable=False)
    
    usuario: "Usuario" = Relationship(back_populates="enderecos")