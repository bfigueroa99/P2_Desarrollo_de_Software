# Generated by Django 4.2.5 on 2023-09-26 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nivel',
            field=models.FloatField(default=1.0),
        ),
    ]
