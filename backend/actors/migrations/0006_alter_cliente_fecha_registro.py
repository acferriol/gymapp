# Generated by Django 4.1.2 on 2024-02-06 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actors", "0005_alter_cliente_fecha_registro_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="fecha_registro",
            field=models.DateField(default=datetime.date(2024, 2, 6)),
        ),
    ]
