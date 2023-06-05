from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.listarClientes),
    path("clientes/<int:id>", views.detalheCliente),
    path("categorias/", views.tipoCategoria),
    path("categorias/<int:id>", views.detalheCategoria),
    path("produtos/", views.tipoProduto),
    path("produtos/<int:id>", views.detalheProduto),
    path("pedidos/", views.tipoPedidos),
    path("pedidos/<int:id>", views.detalheProduto),
    path("pedidosItens/", views.tipoPedidosItens),
    path("pedidosItens/<int:id>", views.detalhePedidosItens),
    ]