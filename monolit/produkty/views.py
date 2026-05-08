from django.shortcuts import get_object_or_404, render

from .models import Kategoria, Producent, Produkt


def produkt_list(request):
    produkty = Produkt.objects.select_related('kategoria', 'producent').all()
    return render(
        request,
        'produkty/list.html',
        {'produkty': produkty},
    )


def produkt_detail(request, produkt_id):
    produkt = get_object_or_404(
        Produkt.objects.select_related('kategoria', 'producent'),
        id=produkt_id,
    )
    return render(
        request,
        'produkty/detail.html',
        {'produkt': produkt},
    )


def kategoria_list(request):
    kategorie = Kategoria.objects.all()
    return render(
        request,
        'produkty/kategoria_list.html',
        {'kategorie': kategorie},
    )


def kategoria_detail(request, slug):
    kategoria = get_object_or_404(Kategoria, slug=slug)
    produkty = kategoria.produkty.select_related('producent').all()
    return render(
        request,
        'produkty/kategoria_detail.html',
        {'kategoria': kategoria, 'produkty': produkty},
    )


def producent_list(request):
    producenci = Producent.objects.all()
    return render(
        request,
        'produkty/producent_list.html',
        {'producenci': producenci},
    )
