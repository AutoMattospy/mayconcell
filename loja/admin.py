from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Produto, Servico, ImagemProduto

class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 3
    fields = ('imagem', 'imagem_preview', 'ordem')
    readonly_fields = ('imagem_preview',)
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.imagem.url)
        return "-"
    imagem_preview.short_description = 'Pré-visualização'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'valor', 'disponivel', 'admin_imagem_preview')
    list_filter = ('categoria', 'disponivel')
    search_fields = ('nome', 'descricao')
    inlines = [ImagemProdutoInline]
    
    def admin_imagem_preview(self, obj):
        if obj.imagem_principal:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.imagem_principal.url)
        return "Sem imagem"
    admin_imagem_preview.short_description = 'Imagem Principal'

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'custo_base', 'disponivel')
    search_fields = ('nome', 'descricao')

admin.site.site_header = "Mayconcell - Administração"
admin.site.site_title = "Mayconcell"
admin.site.index_title = "Bem-vindo ao painel de administração"

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Servico, ServicoAdmin)