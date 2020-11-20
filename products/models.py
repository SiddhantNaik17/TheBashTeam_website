import pytz
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Model for storing product categories"""

    class Meta:
        verbose_name_plural = 'Product Categories'

    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='sub_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


class Product(models.Model):
    """Model for storing products"""

    name = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    motorcycles_supported = models.ManyToManyField(
        'motorcycles.Motorcycle', blank=True, related_name='products')

    description = models.TextField()
    country = models.CharField(max_length=2, choices=pytz.country_names.items(), verbose_name='Country of Origin')

    mrp = models.DecimalField(decimal_places=2, max_digits=20)
    selling_price = models.DecimalField(decimal_places=2, max_digits=20)
    stock = models.IntegerField(default=0)

    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'category': self.category.name, 'slug': self.slug})

    def add_image(self, image):
        ins = ProductImage(product=self, src=image)

        # Set the first image as default
        if not self.images.exists():
            ins.default = True
        ins.save()


class ProductImage(models.Model):
    """Model for storing product images"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to='product_images')
    default = models.BooleanField(default=False)
