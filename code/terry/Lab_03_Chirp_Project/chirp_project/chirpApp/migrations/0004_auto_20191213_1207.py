# Generated by Django 3.0 on 2019-12-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirpApp', '0003_auto_20191213_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='body_text',
            field=models.TextField(max_length=128, verbose_name='Chirp\n'),
        ),
    ]
