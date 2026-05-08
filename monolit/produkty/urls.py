from django.urls import path

from . import views

app_name = 'produkty'

urlpatterns = [
    path('', views.produkt_list, name='produkt_list'),
    path('produkt/<int:produkt_id>/', views.produkt_detail, name='produkt_detail'),
    path('kategorie/', views.kategoria_list, name='kategoria_list'),
    path('kategoria/<slug:slug>/', views.kategoria_detail, name='kategoria_detail'),
    path('producenci/', views.producent_list, name='producent_list'),
]
