# Generated by Django 4.1 on 2022-08-26 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeropuerto_app', '0005_usuario_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
