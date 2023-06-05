from rest_framework import serializers
from .models import *

# O serializaer serve para converter o obj do banco para json e obj json para obj do banco


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields=['id','nome','email','cpf','celular','data_nascimento','data_cadastro','tipo_cliente']

class ProdutoSerializer(serializers.ModelSerializer):
    # nomeCategoria = serializers.CharField(source='categoria.nome')

    class Meta:
        model = Produtos
        fields=['id','nome','preco','qtd','disponibilidade','descricao','categoria']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields=['id','nome']

class FornecedoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedores
        fields=['id','empresa_nome','cnpj','categoria_fornecida','contato_email','telefone','data_cadastro']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields=['id','cliente','data_pedido','status_pedido','metodo_pagamento','total_pagamento','status_pagamento']

class PedidoItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosItens
        fields=['id','fk_produtos','fk_pedidos','qtd','preco_atual','preco_total']
