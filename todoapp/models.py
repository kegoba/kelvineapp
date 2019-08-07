from django.db import models

# Create your models here.

class Record2 (models.Model):
    id = models.AutoField( primary_key=True)
    name  = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
