from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    @property
    def imagem_principal(self):
        primeira_imagem = self.imagens.filter(ordem=0).first()
        return primeira_imagem.imagem if primeira_imagem else None
    
    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    custo_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    @property
    def imagem_principal(self):
        primeira_imagem = self.imagens.filter(ordem=0).first()
        return primeira_imagem.imagem if primeira_imagem else None
    
    def __str__(self):
        return self.nome


class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='produtos/imagens/')
    ordem = models.PositiveIntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem']
        
    def __str__(self):
        return f"Imagem {self.id} - {self.produto.nome}"


class ImagemServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='servicos/imagens/')
    ordem = models.PositiveIntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem']
        
    def __str__(self):
        return f"Imagem {self.id} - {self.servico.nome}"
