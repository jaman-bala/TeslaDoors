from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'number_doc', 'image', 'date',)
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Название",
                       }),

            "number_doc": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Номер договора",
                       }),

            "image": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "",
                       }),
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),


        }
