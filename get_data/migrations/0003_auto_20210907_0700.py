# Generated by Django 3.2.7 on 2021-09-07 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0002_auto_20210905_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_issued',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='get_data.user'),
        ),
        migrations.AlterField(
            model_name='userpayment',
            name='id_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='get_data.user'),
        ),
    ]
