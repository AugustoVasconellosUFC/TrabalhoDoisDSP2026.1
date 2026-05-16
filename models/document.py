"""
--TEMPORARIO REMOVER ANTES DA ENTREGA FINAL--
JUSTIFICATIVA DE CRIAÇÃO:
Entidade estritamente exigida pelas regras do Trabalho Prático. Ela NÃO armazena o
arquivo em si, mas sim os metadados (tipo, tamanho, nome original) dos arquivos
físicos salvos no sistema local. Possui relação muitos-para-um (N:1) com a entidade 'Produto'.
"""
from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship

class Document(SQLModel, table=True):
    __tablename__ = "document"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    original_filename: str = Field(nullable=False)
    content_type: str = Field(nullable=False)
    extension: str = Field(nullable=False)
    size_bytes: int = Field(nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    produto_id: int = Field(foreign_key="produto.id", nullable=False)
    
    produto: "Produto" = Relationship(back_populates="documentos")