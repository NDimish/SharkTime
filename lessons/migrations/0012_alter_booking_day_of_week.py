# Generated by Django 4.1.3 on 2022-12-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_alter_booking_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day_of_week',
            field=models.CharField(choices=[(4, 'Friday'), (1, 'Tuesday'), (0, 'Monday'), (2, 'Wednesday'), (3, 'Thursday')], max_length=1),
        ),
    ]
