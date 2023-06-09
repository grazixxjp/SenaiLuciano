# Generated by Django 4.1.6 on 2023-02-24 16:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0006_alter_pedidoitens_precoatual_alter_pedidoitens_qtd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoitens',
            name='pedidos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vendas.pedidos'),
        ),
        migrations.AlterField(
            model_name='pedidoitens',
            name='produtos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vendas.produtos'),
        ),
        migrations.AlterField(
            model_name='pedidoitens',
            name='qtd',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'A quantidade não pode ser menor que 1')]),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='statusPedido',
            field=models.CharField(choices=[('Em Caminho', 'A Caminho'), ('Preparando', 'Preparando'), ('X', 'Cancelado'), ('Entregue', 'Entregue'), ('Aguardando', 'Aguardando')], default='Aguardando', max_length=255),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='valorTotal',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
