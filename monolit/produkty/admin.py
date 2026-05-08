from django.contrib import admin

from .models import Kategoria, Producent, Produkt


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'slug', 'aktywna')
    prepopulated_fields = {'slug': ('nazwa',)}


@admin.register(Producent)
class ProducentAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'kraj', 'rok_zalozenia')


@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'kategoria', 'producent', 'cena', 'stan_magazynowy')
    list_filter = ('kategoria', 'producent')
    search_fields = ('nazwa', 'opis')
