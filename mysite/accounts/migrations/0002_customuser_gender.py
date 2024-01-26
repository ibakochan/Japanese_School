# Generated by Django 4.2.7 on 2024-01-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "男性"), ("Female", "女性")],
                max_length=10,
                null=True,
            ),
        ),
    ]