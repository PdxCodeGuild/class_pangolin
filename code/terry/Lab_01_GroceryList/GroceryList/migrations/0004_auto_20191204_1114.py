# Generated by Django 3.0 on 2019-12-04 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GroceryList', '0003_auto_20191204_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='complete_date',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='pub_date',
        ),
    ]
