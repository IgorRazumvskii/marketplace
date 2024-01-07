from django import forms
from market.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=ProcessLookupError, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)