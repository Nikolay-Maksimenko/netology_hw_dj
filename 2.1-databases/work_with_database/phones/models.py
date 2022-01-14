from django.db import models



class Phone(models.Model):
    name = models.TextField(null=True)
    price = models.FloatField(null=True)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(null=True)

