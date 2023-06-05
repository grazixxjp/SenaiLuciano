# Generated by Django 4.2 on 2023-05-02 17:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=30)),
                ('id_fiscal', models.CharField(max_length=20, unique=True)),
                ('rg', models.CharField(max_length=13, unique=True)),
                ('foto', models.ImageField(upload_to='pessoas')),
                ('dt_nascimento', models.DateField()),
                ('dt_abertura', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField()),
                ('agencia', models.IntegerField()),
                ('tipo', models.CharField(choices=[('S', 'SALARIO'), ('D', 'DEPOSITO'), ('P', 'PAGAMENTO')], default='D', max_length=1)),
                ('numero', models.IntegerField()),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=11)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fastbank.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateTimeField()),
                ('operacao', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fastbank.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('C', 'CRIPTOMOEDA'), ('A', 'AÇÃO'), ('P', 'POUPANÇA')], default='C', max_length=1)),
                ('aporte', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser igual ou maior que 1 real')])),
                ('taxaAdministracao', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser igual ou maior que 1 real')])),
                ('prazo', models.DateField()),
                ('grauRisco', models.CharField(choices=[('A', 'ALTO'), ('M', 'MEDIO'), ('B', 'BAIXO')], default='M', max_length=1)),
                ('rentabilidade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('finalizado', models.BooleanField()),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fastbank.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fastbank.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_solicitacao', models.DateField(auto_now=True)),
                ('valor_solicitado', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser igual ou maior que 1 real')])),
                ('juros', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser igual ou maior que 1 real')])),
                ('numero_parcela', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser igual ou maior que 1 real')])),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser igual ou maior que 1 real')])),
                ('aprovado', models.BooleanField()),
                ('dt_aprovado', models.DateField(null=True)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fastbank.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=14)),
                ('ramal', models.IntegerField(null=True)),
                ('observacao', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fastbank.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('limite', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser igual ou maior que 1 real')])),
                ('validade', models.DateField()),
                ('cvv', models.IntegerField()),
                ('bandeira', models.CharField(max_length=60)),
                ('situacao', models.CharField(choices=[('B', 'BLOQUEADO'), ('D', 'DESBLOQUEADO')], default=(('B', 'BLOQUEADO'), ('D', 'DESBLOQUEADO')), max_length=1)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fastbank.conta')),
            ],
        ),
    ]
