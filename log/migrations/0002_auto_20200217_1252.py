# Generated by Django 3.0.3 on 2020-02-17 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='in_out',
            new_name='what',
        ),
    ]
