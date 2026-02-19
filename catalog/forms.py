from django import forms

from catalog.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug", "description", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),
            "slug": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите ID"}),
            "order": forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "placeholder": "Введите описание"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-select"}), label="Категория")

    class Meta:
        model = Product
        fields = ["category", "name", "description", "price", "is_active", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),

            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите описание"}),
        }
