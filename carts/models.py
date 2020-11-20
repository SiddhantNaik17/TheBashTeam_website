from django.conf import settings
from django.db import models
from django.db.models import F

from products.models import Product

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def get(self, request):
        if request.user.is_authenticated:
            user_cart, _ = self.model.objects.get_or_create(user=request.user)
            # Check if a cart was created during anonymous session
            # If yes then merge the session cart with the user's persistent cart
            cart_id = request.session.get('cart_id', None)
            if cart_id is not None:
                qs = self.get_queryset().filter(id=cart_id)
                if qs.exists():
                    session_cart = qs.first()
                    CartManager.merge_carts(user_cart, session_cart)
                    del request.session['cart_id']
            return user_cart
        else:
            cart_id = request.session.get('cart_id', None)
            session_cart, _ = self.model.objects.get_or_create(id=cart_id)
            request.session['cart_id'] = session_cart.id
            return session_cart

    @classmethod
    def merge_carts(cls, cart1, cart2):
        for product in cart2.products.all():
            p, _ = cart1.products.get_or_create(product=product.product)
            p.quantity = F('quantity') + product.quantity
            p.save()
        cart2.delete()


class Cart(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='cart')
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def add_product(self, product_id, quantity):
        product = Product.objects.get(id=product_id)
        p, _ = self.products.get_or_create(product=product)
        p.quantity = F('quantity') + quantity
        self.total = F('total') + (product.mrp * quantity)
        self.subtotal = F('subtotal') + (product.selling_price * quantity)
        self.save()
        p.save()

    def remove_product(self, product_id):
        product = Product.objects.get(id=product_id)
        p = self.products.get(product=product)
        self.total = F('total') - (p.product.mrp * p.quantity)
        self.subtotal = F('subtotal') - (p.product.selling_price * p.quantity)
        self.save()
        p.delete()


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
