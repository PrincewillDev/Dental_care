# Generated by Django 5.1.3 on 2024-11-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='preferred_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='preferred_time',
            field=models.CharField(max_length=50),
        ),
    ]
