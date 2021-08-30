from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TextForm, TaplinkAvatarForm, MessengerForm
from .models import TaplinkText, Taplink, Messenger

User = get_user_model()


class TaplinkPageView(LoginRequiredMixin, TemplateView):
    """Homepage class"""

    template_name = 'pages/index.html'
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text_form'] = TaplinkText.objects.filter(taplink=self.request.user.taplink)
        context['text'] = TextForm
        context['social_network'] = Messenger.objects.filter(taplink=self.request.user.taplink)
        context['social_form'] = MessengerForm
        context['avatar_form'] = TaplinkAvatarForm
        context['taplink'] = Taplink.objects.filter(user=self.request.user).prefetch_related('messengers')
        return context


class AddTaplinkTextView(LoginRequiredMixin, FormView):
    """Class for adding texts"""

    template_name = 'pages/index.html'
    form_class = TextForm

    def form_valid(self, form):
        taplink = Taplink.objects.filter(user=self.request.user).first()
        TaplinkText.objects.create(
            taplink=taplink,
            text=form.cleaned_data['text']
        )
        return redirect('home')


class AvatarView(LoginRequiredMixin, FormView):
    """Class for updating users avatar"""

    form_class = TaplinkAvatarForm
    template_name = 'pages/index.html'

    def form_valid(self, form):
        taplink = Taplink.objects.filter(user=self.request.user).first()
        taplink.avatar = form.cleaned_data['avatar']
        taplink.save()
        return redirect('home')


class MessengerAddView(LoginRequiredMixin, FormView):
    """Class for adding link to messengers"""

    form_class = MessengerForm
    template_name = 'pages/index.html'

    def form_valid(self, form):
        taplink = Taplink.objects.filter(user=self.request.user).first()
        Messenger.objects.create(
            taplink=taplink,
            whatsapp=form.cleaned_data['whatsapp'],
            telegram=form.cleaned_data['telegram']
        )
        return HttpResponseRedirect(reverse('home'))
