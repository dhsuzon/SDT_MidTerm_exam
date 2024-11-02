# Generated by Django 4.1.9 on 2024-11-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_carmodel_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='owner',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
