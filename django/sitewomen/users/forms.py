from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.TextInput())
    password2 = forms.CharField(label='Password', widget=forms.TextInput())

    class Meta:
        model=get_user_model()
        fields=['username', 'email', 'first_name', 'last_name', 'password', 'password2']

    def clean_passowrd2(self):
        cd =self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError("Passwords don't matched!")
        else:
            return cd['password']

    def clean_email(self):
        email=self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists")
        else:
            return email