# Generated by Django 4.2.5 on 2023-09-12 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_pregunta_alternativa1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='imagen',
        ),
    ]
