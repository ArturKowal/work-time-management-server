# Generated by Django 3.0.3 on 2020-02-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200211_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data dołączenia '),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Imie '),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Ostatnio zalogowany'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Nazwisko '),
        ),
        migrations.AlterField(
            model_name='account',
            name='stake',
            field=models.FloatField(default=0, verbose_name='Stawka netto'),
        ),
    ]
