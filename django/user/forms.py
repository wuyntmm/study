from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', ]
        labels = {
            'first_name': 'Name',
            'last_name': 'Last name',
            'age': 'Age',
        }
