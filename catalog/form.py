from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='логин', help_text='')
    password1 = forms.CharField(label='пароль',help_text='', widget=forms.PasswordInput)
    password2 = forms.CharField(label='подтверждение', help_text='', widget=forms.PasswordInput)
    email = forms.EmailField(label='почта', widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}))
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(label='Фамилия', max_length=20, required=False)


    class Meta():
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')

