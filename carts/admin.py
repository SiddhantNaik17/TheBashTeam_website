from django.contrib import admin

from carts.models import Cart, CartProduct


class ChoiceInline(admin.StackedInline):
    model = CartProduct
    extra = 1


class CartAdmin(admin.ModelAdmin):
    fields = ['user', 'subtotal', 'total']
    inlines = [ChoiceInline]


admin.site.register(Cart, CartAdmin)
