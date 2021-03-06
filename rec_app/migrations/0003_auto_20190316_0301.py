# Generated by Django 2.1.4 on 2019-03-16 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_app', '0002_auto_20190316_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruitment',
            name='hostel',
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('\\d{10,10}', 'Number must be 10 digits', 'Invalid number')]),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='reg_no',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('\\d{8,8}', 'Registration Number must be 8 digits', 'Invalid Registration Number')]),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='room_no',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('\\d{1,5}')]),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('\\d{4,4}')]),
        ),
    ]
