# Generated by Django 3.2.7 on 2021-09-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210917_1323'),
        ('get_data', '0009_auto_20210920_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_to_products', to='product.Product'),
        ),
    ]
