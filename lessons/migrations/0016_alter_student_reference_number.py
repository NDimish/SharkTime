# Generated by Django 4.1.3 on 2022-12-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0015_alter_student_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reference_number',
            field=models.CharField(default='', max_length=4, null=True),
        ),
    ]
