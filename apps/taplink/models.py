from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()


class Taplink(models.Model):
    """Class for creating Taplink"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='taplink')
    avatar = models.ImageField(upload_to='image', verbose_name='Фото', null=True, blank=True)
    slug = models.SlugField(verbose_name='Ссылка', blank=True)

    class Meta:
        verbose_name = 'Таплинк'
        verbose_name_plural = 'Таплинки'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('text', kwargs={'slug': self.slug})


class Messenger(models.Model):
    """Class for messengers link"""

    taplink = models.ForeignKey(
        Taplink, verbose_name='Привязанный таплинк',
        on_delete=models.CASCADE,
        related_name='taplink'
    )
    whatsapp = models.CharField(
        verbose_name='Ссылка на WhatsApp',
        max_length=70,
        null=True,
        blank=True
    )
    telegram = models.CharField(
        verbose_name='Ссылка на Telegram',
        max_length=70,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Мессенджер таплинка'
        verbose_name_plural = 'Мессенджеры таплинка'


class TaplinkText(models.Model):
    """Class for adding description of taplink"""

    taplink = models.ForeignKey(
        Taplink,
        verbose_name="Привязанный таплинк",
        related_name="taplink_texts",
        on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name='Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'Текст таплинка'
        verbose_name_plural = 'Тексты таплинка'


def post_save_receiver(instance, created, **kwargs):
    if created:
        Taplink.objects.create(user=instance)
        instance.taplink.save()


post_save.connect(post_save_receiver, sender=User)
