from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=17, decimal_places=2)
    summary = models.TextField(blank=True)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        # option one - dynamic
        return reverse('product_detail_view', kwargs={'id': self.pk})

    '''
    option 2 - hard coded
    return f"products/{self.pk}/"
    '''
