from django.db import models


class Buses(models.Model):
    yatayat = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()


class Driver(models.Model):
    name = models.CharField(max_length=200)
    experience = models.CharField(max_length=1500)
    number = models.CharField(max_length=10)
    busnumber = models.CharField(max_length=20)
    fare = models.IntegerField()





