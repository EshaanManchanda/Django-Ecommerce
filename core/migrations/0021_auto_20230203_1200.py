# Generated by Django 2.2.14 on 2023-02-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20230203_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
