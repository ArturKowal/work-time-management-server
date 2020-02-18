# Generated by Django 3.0.3 on 2020-02-11 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_out', models.BooleanField(choices=[(True, 'Wchodze'), (False, 'Wychodze')], default=True)),
                ('when_in', models.DateTimeField(auto_now_add=True, verbose_name='Kiedy ')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Log ',
                'verbose_name_plural': 'Logi ',
            },
        ),
    ]
