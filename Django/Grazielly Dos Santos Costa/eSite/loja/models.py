from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator,MaxValueValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    def __str__(self) -> str:
        return self.nome  
    class Meta:
        verbose_name_plural = "Categoria"  

class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real'),MaxValueValidator(1000)], max_digits=6, decimal_places=2)
    qtd = models.IntegerField(validators=[MinValueValidator(0,message='A quantidade não deve ser negativa')])
    # categoria = models.CharField(max_length=255)
    disponibilidade= models.BooleanField()
    descricao= models.TextField(default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
    class Meta:
        verbose_name_plural = "Produtos"

class Clientes(models.Model):
    CLIENTE_FREE = 'F'
    CLIENTE_PREMIUM = 'P'
    CLIENTE_MASTER = 'M'
    CLIENTE_CHOICES = (
        (CLIENTE_FREE,'Free'),
        (CLIENTE_PREMIUM, 'Premium'),
        (CLIENTE_MASTER,'Master')
    )
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique= True)
    cpf = models.CharField(max_length=14)
    celular = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now=True)
    tipo_cliente = models.CharField(max_length=1, choices=CLIENTE_CHOICES, default=CLIENTE_FREE)
    
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name_plural = "Clientes"

# class Pedidos(models.Model):

class Fornecedores(models.Model):
    empresa_nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique= True)
    categoria_fornecida = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contato_email = models.EmailField(unique= True)
    telefone = models.CharField(max_length=10)
    data_cadastro = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.empresa_nome 
    
    class Meta:
        verbose_name_plural = "Fonecedores"

class Pedidos(models.Model):
    STATUS_PG_NEGADO = 'N'
    STATUS_PG_ANALISE = 'A'
    STATUS_PG_CONFIRMADO = 'C'
    STATUS_PG_CHOICES = (
        (STATUS_PG_NEGADO,'NEGADO'),
        (STATUS_PG_ANALISE, 'EM ANALISE'),
        (STATUS_PG_CONFIRMADO,'CONFIRMADO')
    )

    STATUS_PD_ENTREGUE = 'E'
    STATUS_PD_CANCELADO = 'X'
    STATUS_PD_CAMINHO = 'C'
    STATUS_PD_PREPARACAO = 'P'
    STATUS_PD_AGUARDANDO = 'A'
    
    STATUS_PD_CHOICES = (
        (STATUS_PD_ENTREGUE,'Entregue'),
        (STATUS_PD_CANCELADO, 'Cancelado'),
        (STATUS_PD_CAMINHO,'à Caminho'),
        (STATUS_PD_CAMINHO,'Preparação'),
        (STATUS_PD_CAMINHO,'Aguardando')
    )

    PAGAMENTO_PIX = 'PI'
    PAGAMENTO_CARTAO_CREDITO = 'CC'
    PAGAMENTO_CARTAO_DEBITO = 'CD'
    PAGAMENTO_BOLETO = 'BO'
    PAGAMENTO_CHOICES = (
        (PAGAMENTO_PIX,'PIX'),
        (PAGAMENTO_CARTAO_CREDITO, 'CARTÃO DE CRÉDITO'),
        (PAGAMENTO_CARTAO_DEBITO, 'CARTÃO DE DÉBITO'),
        (PAGAMENTO_BOLETO,'BOLETO')
    )


    cliente = models.ForeignKey(Clientes, on_delete = models.PROTECT)
    data_pedido = models.DateField(auto_now=True)
    status_pedido = models.CharField(max_length=1, choices=STATUS_PD_CHOICES, default=STATUS_PD_AGUARDANDO)
    metodo_pagamento = models.CharField(max_length=2, choices= PAGAMENTO_CHOICES, default= PAGAMENTO_CARTAO_DEBITO)
    total_pagamento = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real'),MaxValueValidator(1000)], max_digits=10, decimal_places=2)
    status_pagamento = models.CharField(max_length=1, choices=STATUS_PG_CHOICES, default=STATUS_PG_ANALISE)

    class Meta:
        verbose_name_plural = "Pedidos"

    def __str__(self) -> str:
        return str(self.id)



class PedidosItens(models.Model):
    fk_produtos = models.ForeignKey(Produtos, on_delete= models.PROTECT)
    fk_pedidos = models.ForeignKey(Pedidos, on_delete= models.CASCADE)
    qtd = models.IntegerField(validators=[MinValueValidator(1,message='A quantidade deve ser igual ou maior que 1')])
    preco_atual = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)        
    preco_total = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Pedidos Itens"
    
    def __str__(self) -> str:
        return str(self.fk_pedidos.id) 