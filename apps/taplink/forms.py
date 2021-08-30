from django import forms

from .models import Taplink, TaplinkText, Messenger


class TextForm(forms.ModelForm):
    """Form for adding texts"""

    class Meta:
        model = TaplinkText
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'hidden': True})
        }


class TaplinkAvatarForm(forms.ModelForm):
    """Form for updating users avatar"""

    class Meta:
        model = Taplink
        fields = ["avatar"]


class MessengerForm(forms.ModelForm):
    """Form for adding link for messengers"""

    class Meta:
        model = Messenger
        fields = ['whatsapp', 'telegram']
