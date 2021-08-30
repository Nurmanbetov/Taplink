from django.urls import path

from .views import AddTaplinkTextView, AvatarView, TaplinkPageView, MessengerAddView


urlpatterns = [
    path('', TaplinkPageView.as_view(), name='home'),
    path('add-text/', AddTaplinkTextView.as_view(), name='add-text'),
    path('avatar/', AvatarView.as_view(), name='avatar'),
    path('message/', MessengerAddView.as_view(), name='message')
]
