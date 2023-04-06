from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'number_doc', 'adress', 'phone', 'file1', 'file2', 'file3', 'first_name', 'last_name')
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "input",
                        "placeholder": "Вид изделия"}),

            "number_doc": forms.TextInput(
                attrs={"class": "input",
                       "placeholder": "Номер договора",
                       }),

            "adress": forms.TextInput(
                attrs={"class": "input",
                       "placeholder": "Адрес",
                       }),

            "phone": forms.TextInput(
                attrs={"class": "input",
                       "placeholder": "Телефон",
                       }),

            "first_name": forms.TextInput(
                attrs={"class": "input",
                       "placeholder": "Имя",
                       }),

            "last_name": forms.TextInput(
                attrs={"class": "input",
                       "placeholder": "Фамилия",
                       }),

            "file1": forms.FileInput(
                attrs={
                       "placeholder": "Прекрепить файл",
                       }),
            "file2": forms.FileInput(
                attrs={
                       "placeholder": "Прекрепить файл",
                       }),
            
            "file3": forms.FileInput(
                attrs={
                       "placeholder": "Прекрепить файл",
                       }),



        }
