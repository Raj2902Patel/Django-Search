from django.db import models

# Create your models here.

class data(models.Model):
    pname = models.CharField(max_length=100)
    pbrand = models.CharField(max_length=100)
    pprice = models.CharField(max_length=100)
    pstock = models.CharField(max_length=100)

    def __str__(self):
        return self.pbrand