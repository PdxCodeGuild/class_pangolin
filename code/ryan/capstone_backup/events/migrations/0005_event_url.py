# Generated by Django 3.0.2 on 2020-02-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(default='www.none.com'),
        ),
    ]
