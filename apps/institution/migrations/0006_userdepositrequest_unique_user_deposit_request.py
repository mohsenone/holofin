# Generated by Django 4.0.6 on 2022-07-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0005_userdepositrequest_quantity'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userdepositrequest',
            constraint=models.UniqueConstraint(fields=('user', 'deposit_request', 'deposit'), name='unique_user_deposit_request'),
        ),
    ]