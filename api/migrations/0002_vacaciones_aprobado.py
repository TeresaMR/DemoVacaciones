# Generated by Django 5.0.4 on 2024-04-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vacaciones",
            name="aprobado",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]