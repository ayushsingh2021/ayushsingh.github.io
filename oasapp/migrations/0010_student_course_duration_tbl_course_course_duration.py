# Generated by Django 5.1 on 2024-09-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0009_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_duration',
            field=models.CharField(default='3 months', max_length=30),
        ),
        migrations.AddField(
            model_name='tbl_course',
            name='course_duration',
            field=models.CharField(default='3 months', max_length=30),
        ),
    ]
