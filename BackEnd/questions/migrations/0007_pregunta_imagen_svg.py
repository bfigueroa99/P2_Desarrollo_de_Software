# Generated by Django 4.2.5 on 2023-09-22 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_remove_pregunta_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='imagen_svg',
            field=models.FileField(blank=True, null=True, upload_to='preguntas_svg/'),
        ),
    ]
