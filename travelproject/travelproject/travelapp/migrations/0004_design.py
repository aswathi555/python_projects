# Generated by Django 4.1.3 on 2022-11-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_guide1'),
    ]

    operations = [
        migrations.CreateModel(
            name='design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='guides')),
            ],
        ),
    ]
