from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'ID: {self.id}, Name: {self.first_name}'
