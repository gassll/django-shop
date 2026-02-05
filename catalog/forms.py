from django import forms

from catalog.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug", "description", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),
            "slug": forms.TextInput(attrs={"class": "form-control","placeholder": "Введите ID"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3,"placeholder": "Введите описание"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
