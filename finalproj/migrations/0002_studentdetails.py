# Generated by Django 3.2 on 2021-05-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField()),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('gpa', models.IntegerField()),
            ],
        ),
    ]