"""
--TEMPORARIO REMOVER ANTES DA ENTREGA FINAL--
JUSTIFICATIVA DE CRIAÇÃO:
Esta tabela associativa (Link Model) foi criada para resolver o requisito obrigatório
do trabalho de possuir pelo menos um relacionamento muitos-para-muitos (N:M).
Ela serve como a ponte que conecta a entidade 'Pedido' a entidade 'Produto', permitindo
que um único pedido contenha vários produtos e que um mesmo produto esteja presente em
vários pedidos de clientes diferentes.
"""
from sqlmodel import SQLModel, Field

class PedidoProdutoLink(SQLModel, table=True):
    __tablename__ = "pedido_produto_link"
    
    pedido_id: int = Field(foreign_key="pedido.id", primary_key=True)
    produto_id: int = Field(foreign_key="produto.id", primary_key=True)