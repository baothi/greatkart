# Generated by Django 3.2.3 on 2021-06-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line_1',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
