# Generated by Django 4.1.4 on 2022-12-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=70, unique=True)),
            ],
            options={
                'db_table': 'categoria',
                'ordering': ('nome',),
            },
        ),
    ]
