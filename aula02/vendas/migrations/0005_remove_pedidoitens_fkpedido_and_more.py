# Generated by Django 4.1.6 on 2023-02-17 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_rename_pedido_pedidoitens_fkpedido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoitens',
            name='fkPedido',
        ),
        migrations.RemoveField(
            model_name='pedidoitens',
            name='fkProduto',
        ),
    ]
