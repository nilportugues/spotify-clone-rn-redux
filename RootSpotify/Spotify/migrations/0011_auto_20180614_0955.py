# Generated by Django 2.0.6 on 2018-06-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0010_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='music',
        ),
        migrations.AddField(
            model_name='playlist',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]