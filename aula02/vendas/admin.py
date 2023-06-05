import decimal
from django.contrib import admin
from . import models
from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib.admin import SimpleListFilter

# Register your models here.

admin.site.register(models.Categorias)
class Filtro(admin.SimpleListFilter):
        title = 'data de nascimento' 
        parameter_name = 'avaliarEstoque'

        def lookups(self, request, model_admin):
             return [
            ('Zerado', 'Zerado'),
            ('Baixo', 'Baixo'),
            ('Ok', 'Ok'),
        ]

        #lte = menor igual
        #gte = maior igual
        #lt = menor
        #gt = maior
        #req = igual (no django usa apenas o =)

        def queryset(self, request, queryset):
            if self.value() == "Estoque zerado":
                #SELECT FROM * PRODUTOS WHERE QTDI <= 10 AND QTD >+ 1
                return queryset.filter(
                    qtd__=0,
            )
            if self.value() == "Estoque baixo":
                return queryset.filter(
                    qtd__gte=2,
                    qtd__lte=10
            )
            if self.value() == "Estoque Ok":
                return queryset.filter(
                    qtd=11,
            )

@admin.register(models.Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nome','tipoCliente']
    list_editable = ['nome','tipoCliente']
    list_filter = ['tipoCliente']

@admin.register(models.Produtos)
class ProdutosAdmin(admin.ModelAdmin):
        list_display = ['id','nome','preco', 'qtd','avaliarEstoque' ,'categoria', 'validade', 'disponibilade']
        list_editable = ['qtd','preco']
        actions = ['zerarEstoque', 'aumentarPreco30']
        search_fields = ['nome__istartswith']
        list_filter = [Filtro]
    
        @admin.display(ordering='qtd')
        def avaliarEstoque(self, produto):
            if produto.qtd == 0:
                produto.qtd = 0
                produto.save()
                return 'Zerado'
            if produto.qtd < 10:
                return 'Estoque Baixo'
            if produto.qtd == 0:
                return 'Estoque OK'

        @admin.action(description='+30%% no preco')
        def aumentarPreco30(self, request, queryset):
            # percentual = (30/100)
            for produto in queryset:
                    # precoAntigo = float(produto.preco)
                    # precoNovo = precoAntigo + precoAntigo * percentual
                    # produto.preco = precoNovo
                    # produto.save()
                    precoAntigo = produto.preco
                    precoAntigo = ((30/100)*precoAntigo)+precoAntigo
                    queryset.update(preco=precoAntigo)

        @admin.action(description='Zerar Estoque')
        def zerarEstoque(self, request, queryset):
                updated = queryset.update(qtd=0)
                self.message_user(request, ngettext(
                    '%d produto foi atualizado.',
                     '%d produtos foram atualizados.',
                    updated,
                ) % updated, messages.SUCCESS)

@admin.register(models.Fornecedor)
class FornecedoresAdmin(admin.ModelAdmin):
    list_filter = ['nome']

class PedidoItemsInline(admin.TabularInline):
    model = models.PedidoItens
    readonly_fields = ['precoAtual']  

@admin.register(models.Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_filter = ['id','valorTotal', 'cliente',]
    inlines = [PedidoItemsInline]

    def save_formset(self, request, form, formset, change) -> None:
         instances = formset.save(commit=False)
         for instance in instances:
              instance.precoAtual = instance.produtos.preco
              instance.precoTotal = instance.qtd * instance.precoAtual
         return super().save_formset(request, form, formset, change)

    def save_model(self, request, obj, form, change) -> None:
        print(obj.id)
        listaPedidos = models.PedidoItens.objects.filter(pedidos_id = obj.id)
        total = 0
        for i in listaPedidos: 
              total += i.precoAtual*i.qtd
        obj.valorTotal = total
        return super().save_model(request, obj, form, change)
    
    @admin.action(description='Valor Total')
    def valorTotal(self, request, queryset):
        qtd = models.Produtos.objects.get()
     
@admin.register(models.Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
     list_filter = ['valor']   