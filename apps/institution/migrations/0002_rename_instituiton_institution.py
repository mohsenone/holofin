# Generated by Django 4.0.6 on 2022-07-10 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_instituiton_user_institution'),
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instituiton',
            new_name='Institution',
        ),
    ]
