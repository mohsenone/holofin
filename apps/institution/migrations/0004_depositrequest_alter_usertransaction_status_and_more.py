# Generated by Django 4.0.6 on 2022-07-10 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institution', '0003_institution_bank_account_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField(verbose_name='مقدار')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_deposit_requests', to=settings.AUTH_USER_MODEL)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deposit_requests', to='institution.institution')),
            ],
            options={
                'verbose_name': 'درخواست واریز',
                'verbose_name_plural': 'درخواست واریز',
            },
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='status',
            field=models.IntegerField(choices=[(0, 'در انتظار'), (1, 'تایید شده'), (2, 'رد شده')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(0, 'واریز'), (1, 'برداشت'), (2, 'قسط'), (3, 'درخواست واریز')], verbose_name='نوع تراکنش'),
        ),
        migrations.CreateModel(
            name='UserDepositRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deposit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_deposit_requests', to='institution.usertransaction')),
                ('deposit_request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_deposit_requests', to='institution.depositrequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_deposit_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'درخواست واریز',
                'verbose_name_plural': 'درخواست واریز',
            },
        ),
    ]
