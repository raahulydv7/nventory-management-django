from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address"
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None  
            field.widget.attrs.update({'class': 'form-control'})
        
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(   
       label="Username",
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter your username"
            }))
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter your password"
            }))
