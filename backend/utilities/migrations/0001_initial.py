# Generated by Django 4.1.2 on 2024-02-02 16:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("actors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("tipo_memb", models.CharField(max_length=30)),
                ("precio", models.FloatField()),
                ("descripcion", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pagos",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "fecha_pago",
                    models.DateField(
                        default=datetime.datetime(2024, 2, 2, 11, 15, 35, 803214)
                    ),
                ),
                ("importe", models.FloatField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="pagos_cli_rev",
                        to="actors.cliente",
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="pagos_plan_rev",
                        to="utilities.plan",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Notifications",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "recibido",
                    models.BooleanField(default=False, verbose_name="Recibido"),
                ),
                ("mensaje", models.TextField()),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 2, 2, 11, 15, 35, 803213)
                    ),
                ),
                (
                    "destinatarios",
                    models.ManyToManyField(
                        related_name="recib_rev", to="actors.empleado"
                    ),
                ),
                (
                    "remitente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="send_rev",
                        to="actors.empleado",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ClaseParticular",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("hora", models.DateTimeField()),
                ("descripcion", models.CharField(max_length=100)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="clase_part_cli_rev",
                        to="actors.cliente",
                    ),
                ),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="clase_part_emp_rev",
                        to="actors.empleado",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ClaseGrupo",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("hora", models.DateTimeField()),
                ("descripcion", models.CharField(max_length=100)),
                ("capacity", models.IntegerField()),
                (
                    "clientes",
                    models.ManyToManyField(
                        related_name="clase_group_cli_rev", to="actors.cliente"
                    ),
                ),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="clase_group_emp_rev",
                        to="actors.empleado",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
