# Generated by Django 4.2.5 on 2023-09-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_pregunta_imagen_svg'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='hint_utilizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='respondida_correctamente',
            field=models.BooleanField(default=False),
        ),
    ]
