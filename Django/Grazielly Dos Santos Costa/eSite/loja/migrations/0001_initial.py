# Generated by Django 4.1.7 on 2023-03-30 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dataNascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('dataCadastro', models.DateField(auto_now=True)),
                ('tipoCliente', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=50)),
                ('complemento', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(choices=[('P', 'Pix'), ('B', 'Boleto'), ('C', 'Cartão')], default='P', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPedio', models.DateField(auto_now=True)),
                ('precoTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('statusPagamento', models.CharField(choices=[('P', 'Pendente'), ('A', 'Aprovado'), ('N', 'Negado')], default='P', max_length=1)),
                ('statusPedido', models.CharField(choices=[('C', 'Cancelado'), ('E', 'Entregue'), ('A', 'Aguardado'), ('T', 'Transporte'), ('P', 'Preparação')], default='A', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.clientes')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.enderecos')),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtdEstoque', models.PositiveIntegerField()),
                ('disponibilidade', models.BooleanField(default=True)),
                ('foto', models.ImageField(upload_to='produtos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='PedidosItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.pedidos')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.produtos')),
            ],
        ),
    ]
