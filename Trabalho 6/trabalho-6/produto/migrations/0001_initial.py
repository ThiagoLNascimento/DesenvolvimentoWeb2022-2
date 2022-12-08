# Generated by Django 4.1.4 on 2022-12-07 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
                ('qtd_estoque', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtos', to='categoria.categoria')),
            ],
            options={
                'db_table': 'produto',
            },
        ),
    ]
