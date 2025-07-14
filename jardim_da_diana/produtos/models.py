from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE) #Se a categoria for excluída, os produtos associados também serão excluídos
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
