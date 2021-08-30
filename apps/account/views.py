from django.contrib.auth import get_user_model, login
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, FormView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from .forms import RegistrationForm, ChangePasswordForm, PasswordResetForm, PhoneNumberForm
from .firebase import check_token

User = get_user_model()


class UserCreationView(CreateView):
    """Class for creating new user"""

    template_name = "pages/registration.html"
    model = User
    form_class = RegistrationForm
    error_message = 'Форма не валидна!'

    def form_valid(self, form):
        firebase_user = check_token(form.cleaned_data['phone_number'])
        user = form.save(commit=False)
        user.phone_number = firebase_user['phone_number']
        user.save()
        login(request=self.request, user=user)
        return redirect('login')

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Class for editing users personal info"""

    template_name = "pages/edit-profile.html"
    model = User
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    """Class for changing users password through old password"""

    form_class = ChangePasswordForm
    template_name = "pages/change-password.html"
    success_url = reverse_lazy('home')


class PhoneVerificationView(TemplateView):
    """Class which verifies users phone number in JS file"""

    template_name = "pages/registration-number.html"
    success_url = 'registration/'


class PhoneVerificationViewCheck(View):
    """Class which check if user exists in database"""

    def get(self, request):
        phone_number = request.GET.get('phone_number')
        redirect_url = request.build_absolute_uri(reverse('verifier'))
        if User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'false': False})
        return JsonResponse({'url': redirect_url})


class NewPasswordResetView(FormView):
    """Class which sets new password"""

    form_class = PasswordResetForm
    template_name = "pages/password-reset.html"

    def form_valid(self, form):
        firebase_user = check_token(form.cleaned_data['firebase_token'])
        try:
            user = User.objects.get(phone_number=firebase_user['phone_number'])
        except User.DoesNotExist:
            raise ValidationError('Пользователь с таким номером не зарегистрирован.')
        user.set_password(form.cleaned_data['new_password1'])
        user.save(update_fields=['password'])
        return HttpResponseRedirect(reverse('login'))


class PasswordResetVNumberView(TemplateView):
    """Class where users submits phone number in JS file """

    template_name = "pages/password-reset-number.html"


class IsUserExistsView(View):
    """Class which checks if user does not exists in database"""

    def get(self, request):
        phone_number = request.GET.get('phone_number')
        redirect_url = request.build_absolute_uri(reverse('password-reset'))
        if User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'url': redirect_url})
        return JsonResponse({'false': False})


class PhoneNumberView(LoginRequiredMixin, FormView):
    """Class where user can change number"""

    form_class = PhoneNumberForm
    template_name = "pages/change-number.html"
    error_message = 'Форма не валидна'
    success_url = 'change_number'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PhoneNumberView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_phone = form.cleaned_data['phone_number']
        user = self.request.user
        user.phone_number = new_phone
        user.save(update_fields=['phone_number'])
        return HttpResponseRedirect(reverse('check-number'))


class PhoneCheckView(View):
    """Class which check if user exists in database"""

    def get(self, request, *args, **kwargs):
        phone_number = request.GET.get('phone_number')
        redirect_url = request.build_absolute_uri(reverse('change-number'))
        if User.objects.filter(phone_number=phone_number).exists():
            request.session['phone_number'] = phone_number
            return JsonResponse({'false': False})
        return JsonResponse({"url": redirect_url})
