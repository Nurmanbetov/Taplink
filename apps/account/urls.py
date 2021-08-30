from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    PhoneVerificationView, UserCreationView, PasswordResetVNumberView,
    ProfileEditView, ChangePasswordView, PhoneNumberView, NewPasswordResetView,
    PhoneVerificationViewCheck, IsUserExistsView, PhoneCheckView
)

urlpatterns = [
    path('phone_verifier/', PhoneVerificationView.as_view(), name='phone-verifier'),
    path('registration/', UserCreationView.as_view(), name='verifier'),
    path('phone-verify/', PhoneVerificationViewCheck.as_view(), name='phone-verify'),

    path('login/', LoginView.as_view(template_name='pages/sign-in.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile_edit/<int:pk>/', ProfileEditView.as_view(), name="edit"),
    path('old_password_change/', ChangePasswordView.as_view(), name="old-password-change"),

    path('password-reset-number/', PasswordResetVNumberView.as_view(), name="password-reset-number"),
    path('password-reset/', NewPasswordResetView.as_view(), name="password-reset"),
    path('is-user-exists/', IsUserExistsView.as_view(), name="is-user-exists"),

    path('change-number/', PhoneNumberView.as_view(), name="change-number"),
    path('check-number/', PhoneCheckView.as_view(), name="check-number"),
]
