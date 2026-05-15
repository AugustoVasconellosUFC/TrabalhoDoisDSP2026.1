from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .endereco import Endereco
	from .pedido import Pedido
    # from .produto import Produto

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str
    telefone: str
    endereco: Endereco = Relationship(back_populates="usuarios")
    pedidos: list["Pedido"] = Relationship(back_populates="usuarios")
    # produtos: list["Produto"] = Relationship(back_populates="usuario")