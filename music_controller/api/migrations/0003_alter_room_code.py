# Generated by Django 4.2.1 on 2023-07-15 23:37

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_room_votes_to_skip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.code_generator, max_length=8, unique=True),
        ),
    ]
