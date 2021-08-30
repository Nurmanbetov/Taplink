from django.contrib import admin

from .models import Taplink, TaplinkText, Messenger


@admin.register(Taplink)
class TaplinkAdmin(admin.ModelAdmin):
    model = Taplink
    list_display = ['user', 'avatar', 'slug']


@admin.register(TaplinkText)
class TextAdmin(admin.ModelAdmin):
    model = TaplinkText
    list_display = ['taplink', 'text']


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    model = Messenger
    list_display = ['whatsapp', 'telegram', 'taplink']
