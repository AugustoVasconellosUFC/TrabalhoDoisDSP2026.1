from fastapi import FastAPI
from fastapi_pagination import add_pagination
from routes import produtos, usuarios, enderecos, pedidos, administradores

app = FastAPI()

# Rotas
app.include_router(produtos.router)
app.include_router(usuarios.router)
app.include_router(enderecos.router)
app.include_router(pedidos.router)
app.include_router(administradores.router)

add_pagination(app)