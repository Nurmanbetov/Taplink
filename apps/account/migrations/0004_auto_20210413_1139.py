# Generated by Django 3.1.7 on 2021-04-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210413_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, verbose_name='Номер телефона'),
        ),
    ]
