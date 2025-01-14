# Generated by Django 4.1.9 on 2024-10-23 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carname', models.CharField(max_length=40)),
                ('carPrice', models.IntegerField()),
                ('CarDescription', models.TextField()),
                ('CarImage', models.ImageField(upload_to='uploads/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brandmodel')),
            ],
        ),
    ]
