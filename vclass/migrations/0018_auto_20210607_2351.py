# Generated by Django 3.1.1 on 2021-06-07 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vclass', '0017_auto_20210607_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='att_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 7, 18, 21, 16, 965253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 18, 21, 16, 965253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 18, 21, 16, 965253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
