# Generated by Django 2.2.14 on 2023-01-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=25),
        ),
    ]