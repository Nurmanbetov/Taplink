# Generated by Django 3.1.7 on 2021-06-02 08:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('taplink', '0013_auto_20210524_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messenger',
            name='telegram',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Ссылка на Telegram'),
        ),
        migrations.AlterField(
            model_name='messenger',
            name='whatsapp',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=70, null=True, region=None, verbose_name='Ссылка на WhatsApp'),
        ),
    ]
