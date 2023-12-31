# Generated by Django 4.2.4 on 2023-08-26 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_delete_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='introduction',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='message',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projects',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
