# Generated by Django 4.2.4 on 2023-08-29 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_projects_live_demo_link_projects_source_code_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_send',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 11, 3, 52, 254084)),
        ),
    ]