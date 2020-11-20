from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from carts.forms import AddressForm
from carts.models import Cart
from orders.models import Order
from website.mixins import RequestFormAttachMixin


def cart_add_product(request):
    if request.method == 'POST':
        if request.POST['submit'] == 'add_to_cart':
            cart = Cart.objects.get(request)
            product_id = int(request.POST['product-id'])
            quantity = int(request.POST['quantity'])
            cart.add_product(product_id, quantity)
        elif request.POST['submit'] == 'buy_now':
            pass
    return redirect('cart-detail')


class CartDetailView(DetailView):
    model = Cart

    def get_object(self, queryset=None):
        return Cart.objects.get(self.request)


class CheckoutView(RequestFormAttachMixin, FormView):
    form_class = AddressForm
    template_name = 'carts/checkout.html'
    success_url = reverse_lazy('order-confirmed')

    def form_valid(self, form):
        address = form.save()
        cart = Cart.objects.get(self.request)
        order = Order.objects.create(
            user=self.request.user,
            cart=cart,
            shipping_address=address,
            total=cart.subtotal,  # Todo: + shipping charges
        )
        self.request.session['order_id'] = order.id
        return super().form_valid(form)
