from rest_framework import serializers
from .models import Clientes, Categorias, PedidoItens, Pedidos, Produtos

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes 
        fields = ['id', 'nome', 'celular','cpf','dataNascimento', 'dataCadastro','tipoCliente']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias 
        fields = ['id','tipo']

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos 
        fields = ['id','nome', 'qtd', 'preco', 'categoria', 'fornecedor', 'descricao', 'validade', 'disponibilade', 'fornecedor']

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos 
        fields = ['id','valorTotal', 'formaPagamento', 'cliente','statusPedido','statusPagamento']

class PedidosItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItens 
        fields = ['id','qtd','precoAtual','pedidos','precoTotal']
