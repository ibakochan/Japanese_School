# Generated by Django 4.2.7 on 2024-01-10 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_grading"),
    ]

    operations = [
        migrations.CreateModel(
            name="NameToDoLists",
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
                ("name", models.CharField(max_length=200)),
                ("password", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "hashed_password",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ToDoList",
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
                ("title", models.CharField(max_length=200)),
                (
                    "name_to_do_lists",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.nametodolists",
                    ),
                ),
            ],
        ),
    ]
