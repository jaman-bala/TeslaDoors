from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','name', 'number_doc', 'image')
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


        }
