# Generated by Django 4.2.4 on 2023-08-29 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_about_resume_link_contact_email_profile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_send',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 21, 11, 50, 851178)),
        ),
    ]