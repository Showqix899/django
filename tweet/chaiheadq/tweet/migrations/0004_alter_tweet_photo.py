# Generated by Django 5.1 on 2024-08-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_alter_tweet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
