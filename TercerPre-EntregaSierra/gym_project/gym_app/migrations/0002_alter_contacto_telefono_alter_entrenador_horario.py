# Generated by Django 5.0.6 on 2024-07-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gym_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacto",
            name="telefono",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="entrenador",
            name="horario",
            field=models.CharField(max_length=100),
        ),
    ]
