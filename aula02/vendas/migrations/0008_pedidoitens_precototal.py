# Generated by Django 4.1.6 on 2023-02-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0007_alter_pedidoitens_pedidos_alter_pedidoitens_produtos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoitens',
            name='precoTotal',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
