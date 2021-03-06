# Generated by Django 2.0.2 on 2018-03-13 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('autores', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('sigla', models.CharField(max_length=10)),
                ('numero', models.IntegerField(max_length=10)),
                ('logo', models.CharField(max_length=10)),
                ('data_de_inicio', models.DateField(max_length=10)),
                ('data_de_fim', models.DateField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('nome', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=150)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste1.Pessoa')),
                ('curriculo', models.CharField(max_length=200)),
                ('artigos', models.CharField(max_length=100)),
            ],
            bases=('teste1.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste1.Evento')),
                ('issn', models.CharField(max_length=100)),
            ],
            bases=('teste1.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste1.Pessoa')),
                ('cpf', models.CharField(max_length=12)),
            ],
            bases=('teste1.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste1.Pessoa')),
                ('cnpj', models.CharField(max_length=18)),
                ('razaosocial', models.CharField(max_length=100)),
            ],
            bases=('teste1.pessoa',),
        ),
    ]
