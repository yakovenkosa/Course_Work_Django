# Generated by Django 5.1.3 on 2024-11-06 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=150)),
                ("body", models.TextField()),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "ordering": ["subject"],
            },
        ),
        migrations.CreateModel(
            name="Recipient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("full_name", models.CharField(max_length=100)),
                ("comment", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "Получатель",
                "verbose_name_plural": "Получатели",
                "ordering": ["full_name"],
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_send_time",
                    models.DateTimeField(
                        blank=True,
                        help_text="укажите время по формату 2023-10-01 12:00",
                        null=True,
                    ),
                ),
                (
                    "end_time",
                    models.DateTimeField(
                        blank=True,
                        help_text="укажите время по формату 2023-10-01 12:00",
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Создана", "Создана"),
                            ("Запущена", "Запущена"),
                            ("Завершена", "Завершена"),
                        ],
                        default="Создана",
                        max_length=10,
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mail.message"
                    ),
                ),
                ("recipients", models.ManyToManyField(to="mail.recipient")),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
    ]
