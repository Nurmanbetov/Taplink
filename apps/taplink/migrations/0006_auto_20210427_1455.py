# Generated by Django 3.1.7 on 2021-04-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taplink', '0005_auto_20210426_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messenger',
            name='telegram',
            field=models.CharField(max_length=70, verbose_name='Ссылка на телеграм'),
        ),
        migrations.AlterField(
            model_name='text',
            name='headline',
            field=models.CharField(default='Заголовок', max_length=70, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
