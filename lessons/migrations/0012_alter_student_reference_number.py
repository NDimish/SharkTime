# Generated by Django 4.1.3 on 2022-12-08 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_alter_student_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reference_number',
            field=models.IntegerField(default=7065, null=True),
        ),
    ]