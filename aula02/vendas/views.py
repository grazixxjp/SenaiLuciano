from django.shortcuts import get_object_or_404
from .serializer import CategoriaSerializer, ClienteSerializer, PedidosItensSerializer, PedidosSerializer, ProdutosSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Categorias, Clientes, PedidoItens, Pedidos, Produtos
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def listarClientes(request):
        print(request)
        if request.method == "GET":
            #armazenar os resultados da query
            queryset =  Clientes.objects.all()
            serializer = ClienteSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = ClienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            pass

@api_view(['GET', 'PUT', 'DELETE'])
def detalheCliente(request, id):
    # try:
    #     cliente =  Clientes.objects.get(pk=id)
    # except Clientes.DoesNotExist:
    #     return Response("Cliente não encontrado", status=status.HTTP_404_NOT_FOUND)
   
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'GET':
     serializer = ClienteSerializer(cliente)
     return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
                cliente.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tipoCategoria(request):
        print(request)
        if request.method == "GET":
            queryset =  Categorias.objects.all()
            serializer = CategoriaSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = CategoriaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            pass

@api_view(['GET', 'PUT', 'DELETE'])
def detalheCategoria(request, id):
    categoria = get_object_or_404(Categorias)
    if request.method == 'GET':
     serializer = CategoriaSerializer(categoria)
     return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
                categoria.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tipoProduto(request):
        print(request)
        if request.method == "GET":
            queryset =  Produtos.objects.all()
            serializer = ProdutosSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = ProdutosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            pass

@api_view(['GET', 'PUT', 'DELETE'])
def detalheProduto(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    if request.method == 'GET':
     serializer = ProdutosSerializer(produto)
     return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProdutosSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            if produto.qtd > 0:
                 return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                produto.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def tipoPedidos(request):
        print(request)
        if request.method == "GET":
            queryset =  Pedidos.objects.all()
            serializer = PedidosSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = PedidosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            pass

@api_view(['GET', 'PUT', 'DELETE'])
def detalhePedidos(request, id):
    pedidos = get_object_or_404(Pedidos)
    if request.method == 'GET':
     serializer = PedidosSerializer(pedidos)
     return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PedidosSerializer(pedidos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
                pedidos.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def tipoPedidosItens(request):
        print(request)
        if request.method == "GET":
            queryset =  PedidoItens.objects.all()
            serializer = PedidosItensSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = PedidosItensSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            pass

@api_view(['GET', 'PUT', 'DELETE'])
def detalhePedidosItens(request, id):
    pedidosItens = get_object_or_404(PedidoItens, pk=id)
    if request.method == 'GET':
     serializer = PedidosItensSerializer(pedidosItens)
     return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PedidosItensSerializer(pedidosItens, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
                pedidosItens.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)