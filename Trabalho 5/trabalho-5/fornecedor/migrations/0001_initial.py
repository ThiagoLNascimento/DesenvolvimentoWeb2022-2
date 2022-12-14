# Generated by Django 3.2.10 on 2022-12-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.IntegerField(max_length=11)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
            ],
            options={
                'db_table': 'fornecedor',
            },
        ),
    ]
