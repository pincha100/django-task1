from django.contrib import admin
from .models import Game, Buyer


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке
    list_display = ('title', 'cost', 'size')
    # Фильтрация по полям
    list_filter = ('size', 'cost')
    # Поиск по полю title
    search_fields = ('title',)
    # Ограничение количества записей
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке
    list_display = ('name', 'balance', 'age')
    # Фильтрация по полям
    list_filter = ('balance', 'age')
    # Поиск по полю name
    search_fields = ('name',)
    # Ограничение количества записей
    list_per_page = 30
    # Только для чтения поле balance
    readonly_fields = ('balance',)

