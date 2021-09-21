# Generated by Django 3.2.6 on 2021-09-04 13:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CidadesAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ibge', models.IntegerField()),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('usuario', models.ManyToManyField(related_name='cidades_atendidas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
