# Generated by Django 4.0.5 on 2022-08-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0002_add_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipoDocumentoIdentidad',
            field=models.CharField(choices=[('DNI', 'Documento de Identidad'), ('RUC', 'Documento Nacional de Identidad'), ('RUC', 'Registro Único de Contribuyentes'), ('PASAPORTE', 'Pasaporte'), ('OTRO', 'Otro')], default='DNI', max_length=50),
        ),
    ]
