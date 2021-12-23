from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.manufacturer_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(null=True, blank=True)
    product_price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    product_description = models.TextField()


class Cart(models.Model):
    products_count = models.IntegerField()
    full_sum = models.FloatField()


class CartProduct(models.Model):
    cart_id = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
