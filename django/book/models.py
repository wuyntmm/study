from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f'ID: {self.id} - Name: {self.title} byt {self.author} from {self.year} by {self.price}$'

