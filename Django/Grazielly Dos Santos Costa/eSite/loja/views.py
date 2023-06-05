from django.shortcuts import render, get_object_or_404
from .models import Produtos, Clientes, Fornecedores, Categoria, PedidosItens
from rest_framework import status
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

class ListarClientes(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

class DetalharCliente(RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

#DetalharProduto = Regra de quantidade de estoque ao deletar 
class ListarProdutos(ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer
    
#AO ADICIONAR UM ITEM AO PEDIDO SUBTRAIR A QUANTIDADE DO ESTOQUE
#AO EXCLUIR UM ITEM DO PEDIDO, RETORNAR A QUANTIDADE AO ESTOQUE

class DetalheProduto(RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer    

    def delete(self, request, pk):
        produto = get_object_or_404(Produtos, pk=pk)
        if produto.qtd > 0:
            return Response({'message':'Não é possível excluir pois ainda existe no estoque'}, status=status.HTTP_400_BAD_REQUEST)

        produto.delete()
        # self.destroy(request,pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

        # return super().delete(request, *args, **kwargs)
    # def delete(self, request, *args, **kwargs):
    #     produto = get_object_or_404(Produtos, pk=kwargs['pk'])
    #     if produto.qtd > 0 and produto.disponibilidade:
    #         return Response({'message':'Não é possível excluir pois ainda existe no estoque'}, status=status.HTTP_400_BAD_REQUEST)
            
    #     return super().delete(request, *args, **kwargs)

@api_view(['GET','POST'])
def Listar_Clientes(request):
    if request.method == 'GET':
        # Armazena os resultados da query
        queryset = Clientes.objects.all()
        #Setar o serializer do cliente e passar o obj pelo queryset
        serializer= ClienteSerializer(queryset, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = ClienteSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        pass

@api_view(['GET','DELETE','PUT'])
def Detalhes_Clientes(request, id):
    # try:
    #     cliente = Clientes.objects.get(id=id)
      
    # except Clientes.DoesNotExist:
    #     return Response("Cliente não encontrado", status= status.HTTP_404_NOT_FOUND)
    clientes = get_object_or_404(Clientes, pk=id)
    if request.method == 'GET':
        # Armazena os resultados da query
        serializer= ClienteSerializer(clientes)
        return Response(serializer.data)
        
    if request.method == 'DELETE':
        try:
            pedido = Pedidos.objects.filter(cliente=id)
            return Response("Existe um pedido com esse cliente, não pode ser deletado", status= status.HTTP_400_BAD_REQUEST)
        except:
            nome = clientes.nome
            clientes.delete()
            return Response(f"Produto {nome} deletado",status=status.HTTP_202_ACCEPTED)
        
    if request.method == 'PUT':
        serializer= ClienteSerializer(instance= clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Dados Invalidos",status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET','POST'])
def Listar_Produtos(request):
    if request.method == 'GET':
        queryset = Produtos.objects.all()
        serializer= ProdutoSerializer(queryset, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = ProdutoSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        pass

@api_view(['GET','DELETE','PUT'])
def Detalhes_Produtos(request, id):
    produtos = get_object_or_404(Produtos, pk=id)
    if request.method == 'GET':
        # Armazena os resultados da query
        serializer= ProdutoSerializer(produtos)
        return Response(serializer.data)
        
    if request.method == 'DELETE':  
        try:
            pedidosItem = PedidosItens.objects.get(fk_produtos=id)
            return Response("Existe um pedido com esse produto, não pode ser deletado", status= status.HTTP_400_BAD_REQUEST)
        except:
            nome = produtos.nome
            if produtos.qtd > 0:
                return Response('Ainda existe unidades desse produto no estoque', status=status.HTTP_400_BAD_REQUEST)
            produtos.delete()
            return Response(f"Produto {nome} deletado",status=status.HTTP_202_ACCEPTED)

    if request.method == 'PUT':
        serializer= ProdutoSerializer(instance= produtos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Listar_Fornecedores(request):
    if request.method == 'GET':
        queryset = Fornecedores.objects.all()
        serializer= FornecedoreSerializer(queryset, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = FornecedoreSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        pass




@api_view(['GET','DELETE','PUT'])
def Detalhes_Fornecedpres(request, id):
    fornecedores = get_object_or_404(Fornecedores, pk=id)
    if request.method == 'GET':
        # Armazena os resultados da query
        serializer= FornecedoreSerializer(fornecedores)
        return Response(serializer.data)
        
    if request.method == 'DELETE':
        nome = fornecedores.nome
        fornecedores.delete()
        return Response(f"Fornecedor {nome} deletado",status=status.HTTP_202_ACCEPTED)

    if request.method == 'PUT':
        serializer= FornecedoreSerializer(instance= fornecedores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Dados Invalidos",status=status.HTTP_400_BAD_REQUEST)
        



@api_view(['GET','POST'])
def Listar_Categorias(request):
    if request.method == 'GET':
        queryset = Categoria.objects.all()
        serializer= CategoriaSerializer(queryset, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = CategoriaSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        pass


@api_view(['GET','DELETE','PUT'])
def Detalhes_Categorias(request, id):
    categorias = get_object_or_404(Categoria, pk=id)
    if request.method == 'GET':
        # Armazena os resultados da query
        serializer= CategoriaSerializer(categorias)
        return Response(serializer.data)
        
    if request.method == 'DELETE':
        nome = categorias.nome
        categorias.delete()
        return Response(f"Categoria {nome} deletada",status=status.HTTP_202_ACCEPTED)

    if request.method == 'PUT':
        serializer= FornecedoreSerializer(instance= Categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Dados Invalidos",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Listar_Pedidos(request):
    if request.method == 'GET':
        queryset = Pedidos.objects.all()
        serializer= PedidoSerializer(queryset, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = PedidoSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        pass


@api_view(['GET','DELETE','PUT'])
def Detalhes_Pedidos(request, id):
    pedidos = get_object_or_404(Pedidos, pk=id)
    if request.method == 'GET':
        # Armazena os resultados da query
        serializer= PedidoSerializer(pedidos)
        return Response(serializer.data)
        
    if request.method == 'DELETE':
        pedidos.delete()
        return Response(f"Pedido deletado",status=status.HTTP_202_ACCEPTED)

    if request.method == 'PUT':
        serializer= PedidoItensSerializer(instance= Pedidos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Dados Invalidos",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Listar_PedidosItem(request):
    if request.method == 'GET':
        queryset = PedidosItens.objects.all()
        serializer= PedidoItensSerializer(queryset, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = PedidoItensSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        pass


@api_view(['GET','DELETE','PUT'])
def Detalhes_PedidosItens(request, id):
    pedidos_itens = get_object_or_404(PedidosItens, pk=id)
    if request.method == 'GET':
        # Armazena os resultados da query
        serializer= PedidoItensSerializer(pedidos_itens)
        return Response(serializer.data)
        
    if request.method == 'DELETE':
        pedidos_itens.delete()
        return Response(f"Pedido Itens deletado",status=status.HTTP_202_ACCEPTED)

    if request.method == 'PUT':
        serializer= PedidoItensSerializer(instance= PedidosItens, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Dados Invalidos",status=status.HTTP_400_BAD_REQUEST)