# Generated by Django 4.1.3 on 2022-12-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0017_alter_student_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reference_number',
            field=models.CharField(default='<function random_id at 0x7f20beabd240>', max_length=4, null=True),
        ),
    ]