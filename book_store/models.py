from django.db import models

class Book(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    published = models.DateTimeField()

