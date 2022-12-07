from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    endereco = models.CharField(max_length=100)
    telefone = models.IntegerField(max_length=11)
    cnpj = models.CharField(max_length=18, unique=True)

    class Meta:
        db_table = 'fornecedor'

    def __str__(self):
        return self.nome
