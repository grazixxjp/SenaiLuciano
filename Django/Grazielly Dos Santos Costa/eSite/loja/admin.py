from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib.admin import SimpleListFilter
from . import models
from loja.models import PedidosItens, Pedidos
# admin.site.register(models.Produtos)
admin.site.register(models.Categoria)


class EstoqueFilter(SimpleListFilter):
        title = 'estoque_avaliacao' # or use _('country') for translated title
        parameter_name = 'estoque_avaliacao'

        def lookups(self, request, model_admin):
            return[
                    ('zerado', ('Zerado')),
                    ('Baixo', ('Estoque Baixo')),
                    ('OK', ('Estoque OK')),
            ]

        def queryset(self, request, queryset):
            #SELECT * FROM PRODUTOS WHERE QTD <= 10 and QTD >=1
                if self.value() == 'zerado':
                    return queryset.filter(
                        qtd = 0
                    )
                elif self.value() == 'Baixo':
                    return queryset.filter(
                        qtd__lte=9,
                        qtd__gte=1
                    )
                elif self.value() == 'OK':
                    return queryset.filter(
                        qtd__gte=10
                    )
                else:
                    return queryset
# decorator@
@admin.register(models.Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','preco','qtd','categoria','avaliar_estoque','disponibilidade']
    actions=['zerar_estoque','aumentar_preco_30']
    search_fields = ['nome__istartswith']
    list_filter=[EstoqueFilter,]
    
    
    
    @admin.display(ordering='qtd')
    def avaliar_estoque(self,produto):
        if produto.qtd <0:
            produto.qtd = 0
            produto.save()
        elif produto.qtd == 0:
            return 'Zerado'
        elif produto.qtd <10:
            return 'Estoque Baixo'
        else:
            return 'Estoque Ok'

    @admin.action(description='+30 %% no preço')
    def aumentar_preco_30(self,request,queryset):
        porcentual = 0.3
        for produto in queryset:
            preco_antigo = float(produto.preco)
            preco_atual = preco_antigo+(preco_antigo*porcentual)
            produto.preco = preco_atual
            produto.save()
        messages.warning(request, 'Os valores foram atualizados.')


    @admin.action(description='Zerar_estoque')
    def zerar_estoque(self, request, queryset):
        updated = queryset.update(qtd=0)
        self.message_user(request, ngettext(
            '%d quantidade foi atualizada.',
            '%d quantidades foram atualizadas.',
            updated,
        ) % updated, messages.WARNING)

@admin.register(models.Clientes)
class ClientesAdmin(admin.ModelAdmin):
   list_display =['id','nome','tipo_cliente',]
   list_editable=['nome','tipo_cliente']
   list_filter=['tipo_cliente']


@admin.register(models.Fornecedores)
class FornecedoresAdmin(admin.ModelAdmin):
    list_display = ['empresa_nome','cnpj','categoria_fornecida','telefone','contato_email','data_cadastro']



class PedidosItensInline(admin.TabularInline):
    model = PedidosItens
    readonly_fields = ['preco_atual','preco_total']
@admin.register(models.Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ['id','cliente','data_pedido','status_pedido','total_pagamento','status_pagamento']
    readonly_fields = ['total_pagamento']
    inlines = [
        PedidosItensInline
    ]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in instances:
            obj.preco_atual = obj.fk_produtos.preco
            obj.preco_total = obj.preco_atual * obj.qtd    
            if obj.qtd > obj.fk_produtos.qtd:
               messages.error(request, f'Há apenas {obj.fk_produtos.qtd} unidades desse produto.')
               return
            else:
                produto_atual = models.Produtos.objects.get(pk= obj.fk_produtos.id)
                produto_atual.qtd -= obj.qtd
                produto_atual.save()

            obj.save()
        


    def save_model(self,request, obj, form, change):
        lista = models.PedidosItens.objects.filter(fk_pedidos_id = obj.id)
        total = 0
        for i in lista:
            total += i.preco_total
        obj.total_pagamento = total
        if total == 0:
            messages.error(request, f'Error.')
            return
        else:
            return super().save_model(request, obj, form, change)
    

# @admin.register(models.PedidosItens )
# class PedidosItensAdmin(admin.ModelAdmin):
#     list_display = ['fk_produtos','fk_pedidos','qtd','preco_atual']