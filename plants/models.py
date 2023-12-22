from django.db import models

# Create your models here.

class Semeystvo (models.Model):
    nazvanie = models.CharField(max_length=50)

    def __str__(self):
        return self.nazvanie

class Gruppa(models.Model):
    nazvanie = models.CharField(max_length=100)

    def __str__(self):
        return self.nazvanie

class Rastenie(models.Model):
    nazvanie = models.CharField(max_length=50)
    opublikovano =  models.BooleanField(default=False, blank=True)
    data_izmen = models.DateTimeField(blank=True, null=True)
    izobrazhenie = models.CharField(max_length=200, blank=True, null=True)
    opisanie = models.TextField(blank=True, null=True)
    temperatura = models.TextField(blank=True, null=True)
    osveshenie = models.TextField(blank=True, null=True)
    poliv = models.TextField(blank=True, null=True)
    udobrenie = models.TextField(blank=True, null=True)
    vlazhnost = models.TextField(blank=True, null=True)
    peresadka = models.TextField(blank=True, null=True)
    razmnozhenie = models.TextField(blank=True, null=True)
    semeystvo = models.ForeignKey(Semeystvo, on_delete=models.SET_NULL, blank=True, null=True)
    gruppi = models.ManyToManyField(Gruppa,  blank=True)

class Person(models.Model):
    login = models.CharField(max_length=50)
    psswd = models.CharField(max_length=30)
    admn = models.BooleanField(default=False, blank=True)
    izbrannoe = models.ManyToManyField(Rastenie, blank=True)