from typing import List, Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from models.pedido_produto import PedidoProdutoLink

class Pedido(SQLModel, table=True):
    __tablename__ = "pedido"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: str = Field(default="pendente", nullable=False)
    
    usuario_id: int = Field(foreign_key="usuario.id", nullable=False)
    
    usuario: "Usuario" = Relationship(back_populates="pedidos")
    produtos: List["Produto"] = Relationship(
        back_populates="pedidos", 
        link_model=PedidoProdutoLink
    )