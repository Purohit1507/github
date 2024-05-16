# Generated by Django 4.2.7 on 2024-05-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Digital', '0002_rename_departmnent_post_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetAuthorizationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_ps_number', models.CharField(max_length=100)),
                ('applicant_name', models.CharField(max_length=100)),
                ('applicant_email_id', models.EmailField(max_length=254)),
                ('request_date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=15)),
                ('initiator_hod_ps_no', models.CharField(max_length=100)),
                ('initiator_hod_name', models.CharField(max_length=100)),
                ('initiator_hod_email_id', models.EmailField(max_length=254)),
                ('net_request_type', models.CharField(max_length=100)),
                ('copy_to_id', models.CharField(max_length=100)),
                ('copy_from_id', models.CharField(max_length=100)),
                ('application_name', models.CharField(max_length=100)),
                ('justification', models.TextField()),
            ],
        ),
    ]