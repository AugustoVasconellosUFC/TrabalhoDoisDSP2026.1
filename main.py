from fastapi import FastAPI
from fastapi_pagination import add_pagination

# Importação dos arquivos de rotas
#from routes import produtos, usuarios
# Descomentar ou adicionar as importações abaixo
# conforme os arquivos em routes/ forem sendo desenvolvidos.
# from routes import pedidos, enderecos, administradores

app = FastAPI(
    title="API - Trabalho Prático 2",
    description="API assíncrona gerenciando entidades com FastAPI e SQLModel",
    version="1.0.0",
)

# Registro das rotas na aplicação
#app.include_router(produtos.router)
#app.include_router(usuarios.router)
# app.include_router(pedidos.router)
# app.include_router(enderecos.router)
# app.include_router(administradores.router)

# Inicialização global da paginação (Requisito Obrigatório)
add_pagination(app)

@app.get("/", tags=["Health Check"])
async def root():
    """Endpoint básico para testar se a API está no ar."""
    return {"message": "API operante! Acesse /docs para ver a documentação OpenAPI/Swagger."}