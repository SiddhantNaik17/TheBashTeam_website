from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    class Meta:
        verbose_name_plural = 'Addresses'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(max_length=120)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return "{for_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
            for_name=self.name or "",
            line1=self.address_line_1,
            line2=self.address_line_2 or "",
            city=self.city,
            state=self.state,
            postal=self.postal_code,
            country=self.country
        )


class Order(models.Model):

    class Status(models.TextChoices):
        CONFIRMED = 'Confirmed', _('Confirmed')
        CANCELLED = 'Cancelled', _('Cancelled')
        SHIPPED = 'Shipped', _('Shipped')
        DELIVERED = 'Delivered', _('Delivered')
        REFUNDED = 'Refunded', _('Refunded')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey('carts.Cart', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='+')
    shipping_address_final = models.TextField(editable=False, null=True)
    status = models.CharField(max_length=10, default=Status.CONFIRMED, choices=Status.choices)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.cart.user = None
        self.cart.save()

    def get_absolute_url(self):
        return reverse("order-detail", kwargs={'order_id': self.id})
