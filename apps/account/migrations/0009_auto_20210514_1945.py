# Generated by Django 3.1.7 on 2021-05-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True, verbose_name='Номер телефона'),
        ),
    ]
