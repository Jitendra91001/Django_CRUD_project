from django import forms
from django.core import validators
from .models import student

class studentRagistration(forms.ModelForm):
    class Meta:
        model = student
        fields=['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class': 'form-control'}),
        }
        