# Generated by Django 4.2.5 on 2023-09-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_pregunta_tema'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='alternativa1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
