from django.core import validators
from django import forms
from .models import profile

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['name', 'email', 'password', 'marks']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value = True, attrs={'class':'form-control'}),
            'marks' : forms.TextInput(attrs={'class':'percentInput'}),

        }