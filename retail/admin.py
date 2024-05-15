from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from retail.models import Network, Trader, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Отображение торговой сети в панели администратора"""
    list_display = ('title', 'factory', 'provider', 'trader_link')

    def trader_link(self, obj):
        """Ссылка для перехода в карточку трейдера"""
        if obj.trader:
            url = reverse('admin:retail_trader_change', args=[obj.trader.id])
            return format_html('<a href="{}">{}</a>', url, obj.trader)
        return '-'
    trader_link.short_description = 'Трейдер'


@admin.register(Trader)
class TraderAdmin(admin.ModelAdmin):
    """Отображение звена торговой сети в панели администратора"""
    list_display = ('id', 'city', 'title', 'trader_type', 'debt', 'supplier_link')
    list_display_links = ('title',)
    ordering = ('title', 'created_at')
    list_filter = ('city',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        """Ссылка для перехода в карточку поставщика"""
        if obj.supplier:
            url = reverse('admin:retail_trader_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier)
        return '-'
    supplier_link.short_description = 'Поставщик'

    @admin.action(description='Удалить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        """Действие удаления задолженности"""
        updated = queryset.update(debt=0)
        self.message_user(request, f'Задолженность удалена для {updated} объектов.')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение продукта в панели администратора"""
    list_display = ('title', 'mod', 'released_at')
    ordering = ('title', 'mod')
