# Generated by Django 3.0.2 on 2020-02-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(default='#'),
        ),
    ]