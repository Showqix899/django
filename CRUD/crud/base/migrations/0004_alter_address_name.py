# Generated by Django 5.0.6 on 2024-07-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_classroom_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
