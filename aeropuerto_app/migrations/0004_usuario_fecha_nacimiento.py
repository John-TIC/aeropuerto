# Generated by Django 4.1 on 2022-08-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeropuerto_app', '0003_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(default='2022-01-02'),
            preserve_default=False,
        ),
    ]