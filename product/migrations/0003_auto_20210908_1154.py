# Generated by Django 3.2.7 on 2021-09-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deliveries',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='leftovers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='return_product',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='way_waryhous',
            field=models.IntegerField(default=0),
        ),
    ]
