# Generated by Django 4.1.3 on 2022-11-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='guide1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic1', models.ImageField(upload_to='guide')),
                ('pic2', models.ImageField(upload_to='guide')),
                ('pic3', models.ImageField(upload_to='guide')),
                ('pic4', models.ImageField(upload_to='guide')),
            ],
        ),
    ]
