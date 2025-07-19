# seu_app/models.py

from django.db import models

class Categoria(models.Model):
    # ... seu modelo Categoria continua igual ...
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    # ... seus outros campos ...
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lucro = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estoque = models.IntegerField(default=0)
    
    # ADICIONE ESTE CAMPO
    is_mais_vendido = models.BooleanField(default=False, verbose_name="Exibir no carrossel da home")

    def __str__(self):
        return self.nome