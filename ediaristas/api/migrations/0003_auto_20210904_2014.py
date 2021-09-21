# Generated by Django 3.2.6 on 2021-09-04 23:14

import api.models
import django.core.validators
from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cidadesatendimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=localflavor.br.models.BRCPFField(max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto_documento',
            field=models.ImageField(null=True, upload_to=api.models.nome_arquivo_foto, validators=[django.core.validators.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto_usuario',
            field=models.ImageField(null=True, upload_to=api.models.nome_arquivo_documento, validators=[django.core.validators.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome_completo',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='reputacao',
            field=models.FloatField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.IntegerField(choices=[(1, 'Cliente'), (2, 'Diaristas')], null=True),
        ),
    ]