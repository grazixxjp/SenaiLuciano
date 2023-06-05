from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=30)
    id_fiscal = models.CharField(max_length=20, unique= True)
    rg = models.CharField(max_length=13, unique=True)
    foto = models.ImageField(upload_to="pessoas")
    dt_nascimento = models.DateField()
    dt_abertura = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.nome

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Contato(models.Model):
    telefone = models.CharField(max_length=14)
    ramal = models.IntegerField(null=True)
    observacao = models.TextField(max_length=255)
    email = models.EmailField(unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Conta(models.Model):
    CONTA_SALARIO ="S"
    CONTA_DEPOSITO ="D"
    CONTA_PAGAMENTO ="P"
    CONTA_CHOICES = (
        (CONTA_SALARIO,"SALARIO"),
        (CONTA_DEPOSITO, "DEPOSITO"),
        (CONTA_PAGAMENTO,"PAGAMENTO")
    )

    ativo = models.BooleanField()
    agencia = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=CONTA_CHOICES, default=CONTA_DEPOSITO)
    numero = models.IntegerField()
    saldo = models.DecimalField(max_digits=11,decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)


class Emprestimo(models.Model):
    dt_solicitacao = models.DateField(auto_now=True)
    valor_solicitado = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)
    juros = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)
    numero_parcela= models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)
    valor_parcela = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)
    aprovado = models.BooleanField()
    dt_aprovado = models.DateField(null=True)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)

class Movimentacao(models.Model):
    dataHora = models.DateTimeField()
    operacao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)


class Investimento(models.Model):
    TPINVEST_CRIPTO ='C'
    TPINVEST_ACAO ='A'
    TPINVEST_POUP ='P'
    TPINVEST_CHOICES = (
        (TPINVEST_CRIPTO,'CRIPTOMOEDA'),
        (TPINVEST_ACAO, 'AÇÃO'),
        (TPINVEST_POUP,'POUPANÇA')
    )
    RISCO_ALTO ='A'
    RISCO_MEDIO ='M'
    RISCO_BAIXO ='B'
    RISCO_CHOICES = (
        (RISCO_ALTO,'ALTO'),
        (RISCO_MEDIO, 'MEDIO'),
        (RISCO_BAIXO,'BAIXO')
    )
    tipo = models.CharField(max_length=1, choices=TPINVEST_CHOICES, default=TPINVEST_CRIPTO)
    aporte = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)
    taxaAdministracao = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)
    prazo = models.DateField()
    grauRisco = models.CharField(max_length=1, choices=RISCO_CHOICES, default=RISCO_MEDIO)
    rentabilidade = models.DecimalField( max_digits=6, decimal_places=2)
    finalizado = models.BooleanField()
    conta = models.ForeignKey(Conta,on_delete=models.PROTECT)

class Cartao(models.Model):
    SIT_CARTAO_BLOQ = 'B'
    SIT_CARTAO_DES = 'D'
    SIT_CARTAO_CHOICES=(
        (SIT_CARTAO_BLOQ,'BLOQUEADO'),
        (SIT_CARTAO_DES,'DESBLOQUEADO'),
    )
    numero = models.IntegerField()
    limite = models.DecimalField(validators=[MinValueValidator(1,message='O preço deve ser igual ou maior que 1 real')], max_digits=6, decimal_places=2)
    validade = models.DateField()
    cvv = models.IntegerField()
    bandeira = models.CharField(max_length=60)
    situacao = models.CharField(max_length=1, choices=SIT_CARTAO_CHOICES, default=SIT_CARTAO_CHOICES)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)


