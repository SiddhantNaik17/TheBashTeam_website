from django.views.generic import DetailView, CreateView

from products.forms import AddProductForm
from products.models import Product, Category
from website.mixins import RequestFormAttachMixin


class ProductDetailView(DetailView):
    model = Product


class CategoryDetailView(DetailView):
    model = Category


class ProductAddView(RequestFormAttachMixin, CreateView):
    form_class = AddProductForm
    template_name = 'products/add_product.html'
