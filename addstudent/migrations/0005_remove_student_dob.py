# Generated by Django 4.1.1 on 2023-04-24 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addstudent', '0004_alter_student_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='DOB',
        ),
    ]
