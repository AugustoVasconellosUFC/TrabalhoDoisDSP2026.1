from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from models.pedido_produto import PedidoProdutoLink

class Produto(SQLModel, table=True):
    __tablename__ = "produto"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    descricao: str = Field(nullable=False)
    preco: float = Field(nullable=False)
    estoque: int = Field(default=0, nullable=False)
    
    # Chave estrangeira ligando o produto à loja (Correção do código do colega)
    loja_id: int = Field(foreign_key="loja.id", nullable=False)
    
    # Relacionamentos
    loja: Optional["Loja"] = Relationship(back_populates="produtos")
    pedidos: List["Pedido"] = Relationship(
        back_populates="produtos",
        link_model=PedidoProdutoLink
    )
    documentos: List["Document"] = Relationship(back_populates="produto")