# Generated by Django 4.2.9 on 2024-05-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmnent', models.CharField(max_length=150)),
                ('Problem', models.TextField(max_length=150)),
            ],
        ),
    ]
