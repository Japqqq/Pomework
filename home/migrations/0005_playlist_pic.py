# Generated by Django 3.1.3 on 2020-11-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_playlist_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
