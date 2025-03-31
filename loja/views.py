from django.shortcuts import render, get_object_or_404
from .models import Produto, Servico, Categoria

def index(request):
    produtos_destaque = Produto.objects.filter(disponivel=True).prefetch_related('imagens')[:4]
    servicos_destaque = Servico.objects.filter(disponivel=True)[:3]
    return render(request, 'loja/index.html', {
        'produtos': produtos_destaque,
        'servicos': servicos_destaque,
    })

def produtos(request):
    categorias = Categoria.objects.all()
    categoria_selecionada = request.GET.get('categoria')
    
    produtos = Produto.objects.filter(disponivel=True).prefetch_related('imagens')
    if categoria_selecionada:
        produtos = produtos.filter(categoria__id=categoria_selecionada)
    
    return render(request, 'loja/produtos.html', {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': int(categoria_selecionada) if categoria_selecionada else None,
    })

def servicos(request):
    servicos = Servico.objects.filter(disponivel=True)
    return render(request, 'loja/servicos.html', {'servicos': servicos})

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto.objects.prefetch_related('imagens'), pk=pk)
    relacionados = Produto.objects.filter(
        categoria=produto.categoria,
        disponivel=True
    ).exclude(id=produto.id).prefetch_related('imagens')[:4]
    
    imagens_adicionais = produto.imagens.exclude(ordem=0).order_by('ordem')
    
    return render(request, 'loja/detalhe_produto.html', {
        'produto': produto,
        'relacionados': relacionados,
        'imagem_principal': produto.imagem_principal,
        'imagens_adicionais': imagens_adicionais
    })