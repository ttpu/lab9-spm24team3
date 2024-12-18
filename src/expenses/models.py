from django.db import models

# Create your models here.
from django.db import models

class Expense(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title