# Generated by Django 2.1.7 on 2019-02-27 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0002_auto_20190227_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='upload',
            field=models.FileField(upload_to=''),
        ),
    ]
