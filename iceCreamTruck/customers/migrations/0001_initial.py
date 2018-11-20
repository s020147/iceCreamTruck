# Generated by Django 2.1.2 on 2018-11-20 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_first', models.CharField(max_length=25)),
                ('customer_last', models.CharField(max_length=25)),
            ],
        ),
    ]
