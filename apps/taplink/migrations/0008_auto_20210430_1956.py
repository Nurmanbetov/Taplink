# Generated by Django 3.1.7 on 2021-04-30 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taplink', '0007_auto_20210429_2033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Text',
            new_name='TaplinkText',
        ),
        migrations.AlterField(
            model_name='messenger',
            name='taplink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taplink', to='taplink.taplink', verbose_name='Привязанный таплинк'),
        ),
    ]
