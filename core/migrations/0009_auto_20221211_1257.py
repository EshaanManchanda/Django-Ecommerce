# Generated by Django 2.2.14 on 2022-12-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20221211_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='about_us',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]