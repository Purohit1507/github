# Generated by Django 4.2.7 on 2024-05-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FC', '0002_daymenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
