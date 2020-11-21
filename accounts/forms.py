from django import forms
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise forms.ValidationError('Invalid credentials')
        login(request, user)
        return data


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'motorcycles_owned', 'password1', 'password1']

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        email = data.get('email')
        full_name = data.get('full_name')
        motorcycles_owned = data.get('motorcycles_owned')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        User.objects.create_user(
            email=email, password=password1, full_name=full_name, motorcycles_owned=motorcycles_owned
        )
        user = authenticate(request, username=email, password=password1)
        login(request, user)
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'motorcycles_owned']
