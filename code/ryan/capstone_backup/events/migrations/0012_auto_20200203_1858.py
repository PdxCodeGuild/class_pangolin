# Generated by Django 3.0.2 on 2020-02-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20200203_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='locals_pics'),
        ),
    ]
