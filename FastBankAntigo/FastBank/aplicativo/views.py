from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken 

# class ListarDetalharUsuario(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated, )
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

#     def list(self, request, *args, **kwargs):
#         token = request.META.get('HTTP_AUTHORIZATION','').split(' ')[1]
#         print (token)
#         dados = AccessToken(token)
#         usuario = dados['user_id']
#         print (usuario)
#         listaUsuario = Usuario.objects.filter(pk = usuario)
#         return super().create(request, *args, **kwargs)
    
    # def create(self, request, *args, **kwargs):
    #             # dados = request.data
    #     # criar = Usuario.objects.create(email=data['email'])                            
    #     # criar.save()
    #     return super().create(request, *args, **kwargs)

class ClientesViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )  
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    def get_queryset(self):
        queryset = Cliente.objects.all()
        cpf = self.request.query_params.get('cpf')
        if cpf is not None:
            queryset = queryset.filter(id_fiscal=cpf)
            return queryset
        else:
            queryset = Cliente.objects.all()
            return queryset


class EnderecoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )  
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )  
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

    def create(self, request, *args, **kwargs):
                # dados = request.data
        # criar = Contato.objects.create(telefone=data['telefone'])                            
        # criar.save()
        return super().create(request, *args, **kwargs)

class ContaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )  
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    def get_queryset(self):
        queryset = Conta.objects.all()
        id_Cliente = self.request.query_params.get('cliente')
        if id_Cliente is not None:
            queryset = queryset.filter(cliente=id_Cliente)
            return queryset
        else:
            queryset = Conta.objects.all()
            return queryset

class EmprestimoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )  
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )  
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

class InvestimentoViewSet(viewsets.ModelViewSet):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

