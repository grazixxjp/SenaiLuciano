from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Categorias(models.Model):
    tipo = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.tipo
    
    class Meta:
        verbose_name_plural = 'Categorias'


class Fornecedor(models.Model):
    
    FORNECEDORES = 'F'

    tiposFornecedores = [
            (FORNECEDORES, 'F'),
    ]        

    nome = models.CharField(max_length=150)
    email =  models.EmailField(unique=True)
    celular = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    dataNascimento = models.DateField()
    dataCadastro = models.DateField(auto_now=True)
    tipoFornecedor = models.CharField(max_length=1, choices=tiposFornecedores, default='F')
    
    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = 'Fornecedores'

class Clientes(models.Model):
    
    CLIENTEFREE = 'F'
    CLIENTEPREMIUM = 'P'
    CLIENTEMASTER = 'M'

    tiposClientes = [
            (CLIENTEFREE, 'Free'),
            (CLIENTEPREMIUM, 'Premium'),
            (CLIENTEMASTER, 'Master'),
    ]

    nome = models.CharField(max_length=150)
    email =  models.EmailField(unique=True)
    celular = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    dataNascimento = models.DateField()
    dataCadastro = models.DateField(auto_now=True)
    tipoCliente = models.CharField(max_length=1, choices=tiposClientes, default=CLIENTEFREE)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = 'Clientes'


class Pedidos(models.Model):

    CAMINHO = 'Em Caminho'
    PREPARANDO = 'Preparando'
    CANCELADO = 'X'
    ENTREGUE = 'Entregue'
    AGUARDANDO = 'Aguardando'

    statusPedidos = [
        (CAMINHO, 'A Caminho'),
        (PREPARANDO, 'Preparando'),
        (CANCELADO, 'Cancelado'),
        (ENTREGUE, 'Entregue'),
        (AGUARDANDO, 'Aguardando')
    ]

    EMANALISE = 'Em Análise'
    APROVADO = 'Aprovado'
    NEGADO = 'Negado'

    statusPagamento = [
            (EMANALISE, 'Em Análise'),
            (APROVADO, 'Aprovado'),
            (NEGADO, 'Negado')
    ]              

    BOLETO = 'Boleto'
    PIX = 'Pix'
    CARTAOCREDITO = 'Cartão de Crédito'
    CARTAODEBITO = 'Cartão de Débito'

    formasPagamento = [
            (BOLETO, 'Boleto'),
            (PIX, 'Pix'),
            (CARTAOCREDITO, 'Cartão de Crédito'),
            (CARTAODEBITO, 'Cartão de Débito')
    ]      

    valorTotal = models.DecimalField(max_digits=19, decimal_places=2)
    formaPagamento = models.CharField(max_length=255, choices=formasPagamento, default='')
    cliente = models.ForeignKey(Clientes,on_delete=models.PROTECT)
    statusPedido = models.CharField(max_length=255, choices=statusPedidos, default='Aguardando')
    statusPagamento = models.CharField(max_length=255, choices=statusPagamento, default='Em Análise')
   
    def __str__(self) -> str:
        return str(self.id) + '-' + str(self.cliente.nome)

    class Meta:
        verbose_name_plural = 'Pedidos'

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    qtd = models.IntegerField()
    preco = models.DecimalField(max_digits=6,decimal_places=2)
    categoria = models.CharField(max_length=50)
    fornecedor = models.CharField(max_length=50)
    descricao = models.TextField()
    validade = models.DateField()
    disponibilade = models.BooleanField()
    
    #referenciar a categoria aqui
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
   
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Produtos'

class PedidoItens(models.Model):
    qtd = models.IntegerField(validators=[MinValueValidator(1,'A quantidade não pode ser menor que 1')])
    precoAtual = models.DecimalField(max_digits=10,decimal_places=2)

    #referenciar a categoria aqui
    produtos = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    pedidos = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    precoTotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.produtos.nome)
    
    class Meta:
        verbose_name_plural = 'PedidoItens'
    
    
class Carrinho(models.Model):
    produtos = models.ForeignKey(Produtos,on_delete=models.PROTECT)
    qtd = models.IntegerField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    
    pedidos = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = 'Carrinho'
      