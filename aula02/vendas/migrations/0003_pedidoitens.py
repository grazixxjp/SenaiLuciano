# Generated by Django 4.1.6 on 2023-02-17 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_carrinho'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
                ('pedido', models.CharField(max_length=255)),
                ('qtd', models.CharField(max_length=255)),
                ('precoAtual', models.CharField(max_length=255)),
                ('pedidos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.pedidos')),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.produtos')),
            ],
            options={
                'verbose_name_plural': 'PedidoItens',
            },
        ),
    ]
