# Generated by Django 3.2 on 2021-05-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalproj', '0004_rename_studentfname_enrollment_studentname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='classname',
            new_name='coursename',
        ),
    ]
