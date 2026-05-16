from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class Loja(SQLModel, table=True):
    __tablename__ = "loja"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    senha: str = Field(nullable=False)
    
    # Relacionamento: Uma loja tem vários produtos
    produtos: List["Produto"] = Relationship(back_populates="loja")