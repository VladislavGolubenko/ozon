# Generated by Django 3.2.7 on 2021-12-02 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0031_ozontransactions_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ozontransactions',
            name='items',
        ),
    ]
