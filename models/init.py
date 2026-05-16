"""
--TEMPORARIO REMOVER ANTES DA ENTREGA FINAL--
JUSTIFICATIVA DE CRIAÇÃO:
Arquivo essencial para a descoberta de modelos. Ele centraliza as importações de todas as
entidades. Sem este arquivo, o Alembic (gerenciador de migrações) e o SQLModel podem
sofrer com problemas de 'importação circular' e falhar ao gerar as tabelas no banco de dados.
"""
from sqlmodel import SQLModel
from .pedido_produto import PedidoProdutoLink
from .usuario import Usuario
from .endereco import Endereco
from .pedido import Pedido
from .produto import Produto
from .administrador import Administrador
from .document import Document

__all__ = [
    "SQLModel",
    "PedidoProdutoLink",
    "Usuario",
    "Endereco",
    "Pedido",
    "Produto",
    "Administrador",
    "Document"
]