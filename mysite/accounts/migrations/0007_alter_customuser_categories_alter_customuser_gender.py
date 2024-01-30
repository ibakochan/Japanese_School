# Generated by Django 4.2.7 on 2024-01-25 02:14

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_remove_customuser_grading_content_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="categories",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Japanese_Basic_1", "Japanese Basic 1"),
                    ("Japanese_Basic_2", "Japanese Basic 2"),
                    ("Japanese_Basic_3", "Japanese Basic 3"),
                    ("Japanese_Basic_4", "Japanese Basic 4"),
                    ("Japanese_Advanced_1", "Japanese Advanced 1"),
                    ("Japanese_Advanced_2", "Japanese Advanced 2"),
                    ("Japanese_Advanced_3", "Japanese Advanced 3"),
                    ("Japanese_Advanced_4", "Japanese Advanced 4"),
                    ("Japanese_Expert_1", "Japanese Expert 1"),
                    ("Japanese_Expert_2", "Japanese Expert 2"),
                    ("Japanese_Expert_3", "Japanese Expert 3"),
                    ("Japanese_Expert_4", "Japanese Expert 4"),
                    ("Math", "Math"),
                    ("Science", "Science"),
                    ("Social_Studies", "Social Studies"),
                ],
                default=[],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "Male"), ("Female", "Female")],
                max_length=10,
                null=True,
            ),
        ),
    ]