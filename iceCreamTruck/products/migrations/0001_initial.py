# Generated by Django 2.1.2 on 2018-12-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('flavor_i_d', models.AutoField(primary_key=True, serialize=False)),
                ('flavor_name', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
