# Generated by Django 3.2 on 2024-05-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_fechas_recomendadas_alter_vacaciones_fechafinal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacaciones',
            name='idTrabajador',
            field=models.IntegerField(),
        ),
    ]