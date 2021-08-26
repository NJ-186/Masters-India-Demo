from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=20
    )


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    name = models.CharField(
        max_length=20
    )


class Product(models.Model):
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT
    )
    name = models.CharField(
        max_length=20
    )