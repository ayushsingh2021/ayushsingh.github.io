# Generated by Django 5.1 on 2024-09-13 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0005_tbl_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_course',
            old_name='course_session',
            new_name='session',
        ),
    ]
