# Generated by Django 3.0 on 2019-12-04 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0003_auto_20191203_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
