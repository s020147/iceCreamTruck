# Generated by Django 2.1.2 on 2018-12-01 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_delete_productform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderform',
            name='flavor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]