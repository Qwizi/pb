from django.db import models
from django.urls import reverse


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    opis = models.TextField(blank=True)
    aktywna = models.BooleanField(default=True)

    class Meta:
        ordering = ['nazwa']
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('produkty:kategoria_detail', args=[self.slug])


class Producent(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)
    kraj = models.CharField(max_length=80)
    rok_zalozenia = models.PositiveIntegerField()
    strona_www = models.URLField(blank=True)
    opis = models.TextField(blank=True)

    class Meta:
        ordering = ['nazwa']
        verbose_name = 'Producent'
        verbose_name_plural = 'Producenci'

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    stan_magazynowy = models.PositiveIntegerField(default=0)
    data_dodania = models.DateTimeField(auto_now_add=True)
    kategoria = models.ForeignKey(
        Kategoria,
        on_delete=models.CASCADE,
        related_name='produkty',
    )
    producent = models.ForeignKey(
        Producent,
        on_delete=models.PROTECT,
        related_name='produkty',
    )

    class Meta:
        ordering = ['-data_dodania']
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('produkty:produkt_detail', args=[self.id])

    @property
    def dostepny(self):
        return self.stan_magazynowy > 0
