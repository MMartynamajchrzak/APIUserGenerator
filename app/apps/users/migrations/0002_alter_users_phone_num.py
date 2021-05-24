# Generated by Django 3.2 on 2021-05-12 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_num',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='First input country code eg.(+48), then the number.', regex='^\\+\\d{7,15}$')]),
        ),
    ]
