# Generated by Django 4.1.1 on 2023-04-24 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addstudent', '0002_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
