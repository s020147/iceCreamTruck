# Generated by Django 2.1.2 on 2018-12-01 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20181201_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderform',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
