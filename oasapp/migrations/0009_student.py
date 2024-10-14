# Generated by Django 5.1 on 2024-09-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0008_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('emailaddress', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('aadress', models.TextField()),
                ('aadharno', models.CharField(max_length=15)),
                ('aadharpic', models.ImageField(upload_to='')),
                ('session', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=30)),
                ('hs_percent', models.CharField(max_length=10)),
                ('hs_marksheet', models.ImageField(upload_to='')),
                ('inter_percent', models.CharField(max_length=10)),
                ('inter_marksheet', models.ImageField(upload_to='')),
                ('pic', models.ImageField(upload_to='')),
                ('sign', models.ImageField(upload_to='')),
                ('application_status', models.CharField(max_length=1)),
                ('fees', models.IntegerField()),
                ('fees_status', models.CharField(max_length=1)),
                ('fees_ss', models.ImageField(upload_to='')),
                ('status', models.CharField(max_length=1)),
            ],
        ),
    ]
