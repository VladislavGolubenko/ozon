# Generated by Django 3.2.7 on 2021-10-04 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0014_auto_20211004_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='payment_type',
            new_name='type',
        ),
    ]
