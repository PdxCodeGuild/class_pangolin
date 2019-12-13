# Generated by Django 3.0 on 2019-12-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_auto_20191213_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=6)),
                ('long_url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
        migrations.DeleteModel(
            name='Abbreviation',
        ),
        migrations.DeleteModel(
            name='URLManager',
        ),
    ]