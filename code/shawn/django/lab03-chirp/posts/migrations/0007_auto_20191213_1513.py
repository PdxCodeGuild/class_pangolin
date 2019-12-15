# Generated by Django 3.0 on 2019-12-13 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20191211_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chirp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Chirp')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chirp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Chirp')),
            ],
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='chirp',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Reaction',
        ),
    ]