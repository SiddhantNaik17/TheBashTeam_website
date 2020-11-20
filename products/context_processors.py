from products.models import Category


def add_categories_to_context(request):
    riding_gears = Category.objects.filter(parent=1)
    accessories = Category.objects.filter(parent=2)
    parts = Category.objects.filter(parent=3)

    context = {
        'riding_gears': riding_gears,
        'accessories': accessories,
        'parts': parts,
    }

    return context
