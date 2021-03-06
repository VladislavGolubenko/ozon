# Generated by Django 3.2.7 on 2021-10-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0015_rename_payment_type_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='api_key',
            field=models.CharField(default='Null', max_length=500, verbose_name='API ключ OZON'),
        ),
        migrations.AddField(
            model_name='user',
            name='card_ovner',
            field=models.CharField(default='Null', max_length=250, verbose_name='Данные владельца карты'),
        ),
        migrations.AddField(
            model_name='user',
            name='card_yer',
            field=models.CharField(default='Null', max_length=5, verbose_name='Срок действия карты'),
        ),
        migrations.AddField(
            model_name='user',
            name='ozon_id',
            field=models.IntegerField(default=0, verbose_name='ID пользователя OZON'),
        ),
    ]
