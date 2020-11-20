from django import forms

from orders.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']

    def __init__(self, request, *args, **kwargs):
        # Bind request object to the form
        self.request = request
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.request.user
        instance.save()
        return instance
