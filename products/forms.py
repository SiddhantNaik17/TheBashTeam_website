from django import forms

from products.models import Product


class AddProductForm(forms.ModelForm):
    """Form for adding a new product to the store"""

    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Product
        fields = ['name', 'category', 'images', 'description', 'country', 'mrp', 'selling_price', 'stock']

    def __init__(self, request, *args, **kwargs):
        # Bind request object to the form
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        if Product.objects.filter(name=self.cleaned_data['name']).exists():
            raise forms.ValidationError('A product with the same name already exists')
        return super().clean()

    def save(self, commit=True):
        # Save product images properly
        instance = super().save(commit)
        images = self.request.FILES.getlist('images')
        for image in images:
            instance.add_image(image)
        return instance
