# Generated by Django 2.2.14 on 2023-01-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
            ],
        ),
    ]