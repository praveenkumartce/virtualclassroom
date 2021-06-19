# Generated by Django 3.1.1 on 2021-06-06 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vclass', '0014_auto_20210606_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='ass_desc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assignment',
            name='ass_file',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 6, 11, 45, 52, 78854, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 11, 45, 52, 78854, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 11, 45, 52, 78854, tzinfo=utc)),
        ),
    ]
