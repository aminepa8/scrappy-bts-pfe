# Generated by Django 2.2.2 on 2019-06-06 11:13

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=190)),
                ('subject', models.CharField(max_length=120)),
                ('date', models.DateField(default=datetime.date.today)),
                ('discreption', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
