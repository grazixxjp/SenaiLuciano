from django.urls import path
from . import views

urlpatterns = [
    path("clientes-new/", view= views.ListarClientes.as_view()),
    path("cliente/<int:pk>/", view= views.DetalharCliente.as_view()),
    path("produtos-new/", view= views.ListarProdutos.as_view()),
    path("produtos-new/<int:pk>", view= views.DetalheProduto.as_view()),
    path("clientes/", view= views.Listar_Clientes),
    path("clientes/<int:id>/", view= views.Detalhes_Clientes),
    path("produtos/", view= views.Listar_Produtos),
    path("produtos/<int:id>/", view= views.Detalhes_Produtos),
    path("fornecedores/", view= views.Listar_Fornecedores),
    path("fornecedores/<int:id>/", view= views.Detalhes_Fornecedpres),
    path("categorias/", view= views.Listar_Categorias),
    path("categorias/<int:id>/", view= views.Detalhes_Categorias),
    path("pedidos/", view= views.Listar_Pedidos),
    path("pedidos/<int:id>/", view= views.Detalhes_Pedidos),
    path("pedidositens/", view= views.Listar_PedidosItem),
    path("pedidositens/<int:id>/", view= views.Detalhes_PedidosItens),
]