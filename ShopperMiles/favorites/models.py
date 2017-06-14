from __future__ import unicode_literals, absolute_import
from django.db import models

from products.models import Product
from users.models import User


class Favorite(models.Model):
    # additional fields here
    product = models.OneToOneField(
        Product, verbose_name='Producto', on_delete=models.CASCADE, primary_key=False,)
    user = models.ForeignKey(
        User, verbose_name='Usuario', on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        ordering = ['pk']
