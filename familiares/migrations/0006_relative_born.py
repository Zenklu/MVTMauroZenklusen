# Generated by Django 4.0.6 on 2022-07-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0005_remove_relative_born'),
    ]

    operations = [
        migrations.AddField(
            model_name='relative',
            name='born',
            field=models.DateField(max_length=50),
        ),
    ]
