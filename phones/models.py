from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name
