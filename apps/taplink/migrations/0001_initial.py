# Generated by Django 3.1.7 on 2021-04-25 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Taplink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='media', verbose_name='Фото')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taplink', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Таплинк',
                'verbose_name_plural': 'Таплинки',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length='400', verbose_name='Текст')),
                ('taplink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taplink_texts', to='taplink.taplink', verbose_name='Привязанный таплинк')),
            ],
            options={
                'verbose_name': 'Текст таплинка',
                'verbose_name_plural': 'Тексты таплинка',
            },
        ),
        migrations.CreateModel(
            name='Messanger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(max_length=70, verbose_name='Ссылка на ватсапп')),
                ('telegram', models.CharField(max_length=70, verbose_name='Ссылка на телеграс')),
                ('taplink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taplink.taplink', verbose_name='Привязанный таплинк')),
            ],
            options={
                'verbose_name': 'Мессенджер таплинка',
                'verbose_name_plural': 'Мессенджеры таплинка',
            },
        ),
    ]
