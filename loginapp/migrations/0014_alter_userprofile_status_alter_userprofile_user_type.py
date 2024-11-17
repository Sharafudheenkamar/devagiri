# Generated by Django 5.1.3 on 2024-11-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0013_alter_userprofile_status_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('STUDENT', 'student'), ('LABSTAFF', 'Labstaff'), ('FACULTY', 'Faculty'), ('ADMIN', 'Admin')], max_length=20),
        ),
    ]
