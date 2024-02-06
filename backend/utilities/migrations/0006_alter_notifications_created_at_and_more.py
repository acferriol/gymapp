# Generated by Django 4.1.2 on 2024-02-06 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utilities", "0005_alter_notifications_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notifications",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 6, 10, 26, 30, 957953)
            ),
        ),
        migrations.AlterField(
            model_name="pagos",
            name="fecha_pago",
            field=models.DateField(default=datetime.date(2024, 2, 6)),
        ),
    ]
