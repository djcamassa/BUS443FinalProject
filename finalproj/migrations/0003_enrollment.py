# Generated by Django 3.2 on 2021-05-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproj', '0002_studentdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentfname', models.CharField(max_length=200)),
                ('classname', models.CharField(max_length=200)),
            ],
        ),
    ]
