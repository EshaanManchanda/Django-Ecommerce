# Generated by Django 2.2.14 on 2023-02-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20230203_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
