from .models import * 
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields =['id','nome','senha','foto','dt_nascimento','dt_abertura','id_fiscal','rg']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields=['id','logradouro','cidade','bairro','uf','cep','cliente']

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields=['id','telefone','ramal','observacao','email']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields=['id','dt_solicitacao','valor_solicitado','juros','numero_parcela','valor_parcela','aprovado','dt_aprovado','conta']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id','ativo','agencia','tipo','numero','saldo','cliente']

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id','numero','validade','cvv','situacao','bandeira','limite','conta']

class InvestimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimento
        fields = ['id','tipo','aporte','taxaAdministracao','prazo','grauRisco','rentabilidade','finalizado','conta']

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ['id','dataHora','operacao','valor','conta']