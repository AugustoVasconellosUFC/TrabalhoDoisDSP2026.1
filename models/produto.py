from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .loja import Loja
	# from .pedido import Pedido, [WIP: CLASSE ASSOCIATIVA]
    # from .usuario import Usuario

class Produto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    preco: float
    estoque: int
    # pedidos: list["Pedido"] = Relationship(back_populates="produtos", link_model=[CLASSE ASSOCIATIVA])
    # usuario_id: int = Relationship(foreign_key="usuario.id")
    # produtos: Usuario = Relationship(back_populates="usuario")