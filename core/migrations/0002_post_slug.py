# Generated by Django 3.2.4 on 2021-07-04 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='fix-me'),
            preserve_default=False,
        ),
    ]
