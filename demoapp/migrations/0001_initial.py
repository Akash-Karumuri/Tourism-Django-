# Generated by Django 5.1.3 on 2024-11-27 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
