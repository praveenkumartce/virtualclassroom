# Generated by Django 3.1.1 on 2021-06-06 06:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vclass', '0003_auto_20210605_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='att_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 6, 6, 0, 46, 260571, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 6, 0, 46, 260571, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 6, 0, 46, 260571, tzinfo=utc)),
        ),
    ]
