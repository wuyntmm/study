from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'book'
