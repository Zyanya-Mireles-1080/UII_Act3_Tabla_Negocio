# Generated by Django 5.1 on 2024-11-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('id_cliente', models.CharField(max_length=5)),
                ('id_empleado', models.CharField(max_length=5)),
                ('fecha', models.DateField(verbose_name='Fecha del pedido')),
                ('total', models.CharField(max_length=1000000)),
                ('metodo_pago', models.CharField(max_length=20)),
                ('horario', models.TimeField(verbose_name='Horario')),
                ('cantidad', models.CharField(max_length=1000)),
            ],
        ),
    ]
