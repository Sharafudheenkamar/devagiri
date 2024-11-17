# Generated by Django 5.1.1 on 2024-10-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_alter_userprofile_user_type'),
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
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('LABSTAFF', 'Labstaff'), ('STUDENT', 'student'), ('FACULTY', 'Faculty')], max_length=20),
        ),
    ]