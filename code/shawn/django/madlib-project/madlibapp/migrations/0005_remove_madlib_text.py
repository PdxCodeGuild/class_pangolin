# Generated by Django 3.0 on 2019-12-07 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madlibapp', '0004_auto_20191206_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madlib',
            name='text',
        ),
    ]
