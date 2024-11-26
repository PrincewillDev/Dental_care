# Generated by Django 5.1.3 on 2024-11-21 15:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('aid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=70)),
                ('firstname', models.CharField(max_length=70)),
                ('lastname', models.CharField(max_length=70)),
                ('phonenumber', models.CharField(max_length=20)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.TimeField()),
                ('service_type', models.CharField(choices=[('general_check-up', 'general_check-up'), ('teeth_cleaning', 'teeth_cleaning'), ('teeth_whitening', 'teeth_whitening'), ('dental_implants', 'dental_implants'), ('root_canal', 'root_canal'), ('other', 'other')], default='general_check-up', max_length=60)),
                ('additional_note', models.TextField()),
            ],
        ),
    ]