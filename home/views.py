from django.shortcuts import render
from django.views.generic.base import View

from products.models import Category, Product


class HomepageView(View):
    def get(self, request):
        trending_products = Product.objects.filter(active=True, trending=True)

        context = {
            'trending_products': trending_products,
        }
        return render(request, 'home/index.html', context)
