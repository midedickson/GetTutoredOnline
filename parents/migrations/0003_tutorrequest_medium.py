# Generated by Django 3.0.6 on 2020-06-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0002_auto_20200603_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorrequest',
            name='medium',
            field=models.CharField(choices=[('online', 'Online Tutoring'), ('physical', 'Physical Tutoring'), ('both', 'Both')], default='online', max_length=10),
        ),
    ]
