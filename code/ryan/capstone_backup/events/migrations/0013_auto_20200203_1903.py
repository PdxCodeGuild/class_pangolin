# Generated by Django 3.0.2 on 2020-02-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20200203_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='locals_pics'),
        ),
    ]
