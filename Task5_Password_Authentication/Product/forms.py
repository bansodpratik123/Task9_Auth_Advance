from django import forms
from .models import Documents, Laptops

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Documents
        fields=['ModelName','Document']


class LaptopModelForm(forms.ModelForm):
    class Meta:
        model=Laptops
        fields='__all__'