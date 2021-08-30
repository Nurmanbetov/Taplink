from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(UserCreationForm):
    """ Form for creating new user"""

    phone_number = forms.CharField(widget=forms.TextInput(attrs={'id': 'phone_number', 'hidden': True}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]


class ChangePasswordForm(PasswordChangeForm):
    """Overwritten form for changing users password"""

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'class': 'form_input',
                                                                        'placeholder': 'Введите старый пароль'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form_input',
                                                                         'placeholder': 'Введите новый пароль'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form_input',
                                                                         'placeholder': 'Повторите новый пароль'})


class PasswordResetForm(forms.Form):
    """Form used for reset password"""

    firebase_token = forms.CharField(widget=forms.TextInput(attrs={"id": 'firebase_token'}))

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    error_messages = {
        'password_mismatch': 'Пароли не совпадают.',
        'password_short': 'Пароль слишком короткий.',
        'space_in_password': 'Пароль не должен содердать пробелы'
    }

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        if ' ' in password1:
            raise ValidationError(
                self.error_messages['space_in_password'],
                code='space_in_password'
            )
        if len(password2) < 7:
            raise ValidationError(
                self.error_messages['password_short'],
                code='password_short'
            )
        return password2


class PhoneNumberForm(forms.Form):
    """Form used for changing users number"""

    phone_number = forms.CharField(widget=forms.TextInput(attrs={'id': 'phone_number'}))
