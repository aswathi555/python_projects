# Generated by Django 4.1.3 on 2022-11-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
