# Generated by Django 3.2.7 on 2021-10-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0018_auto_20211005_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_ovner',
            field=models.CharField(blank=True, default='Null', max_length=250, null=True, verbose_name='Данные владельца карты'),
        ),
        migrations.AlterField(
            model_name='user',
            name='card_year',
            field=models.CharField(blank=True, default='Null', max_length=5, null=True, verbose_name='Срок действия карты'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный пользователь'),
        ),
    ]
