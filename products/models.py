from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    CATEGORY = (
        ('Cup', 'Cup'),
        ('Plate', 'Plate'),
        ('Bowl', 'Bowl'),
        ('Vase', 'Vase')
    )

    name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


