# Generated by Django 4.1.1 on 2023-04-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('enrollment', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('course', models.CharField(max_length=128)),
                ('year', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('attendance', models.BooleanField(default='False')),
            ],
        ),
    ]
