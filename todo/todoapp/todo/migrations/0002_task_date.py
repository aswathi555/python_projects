# Generated by Django 4.1.3 on 2022-11-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-05-12'),
            preserve_default=False,
        ),
    ]
