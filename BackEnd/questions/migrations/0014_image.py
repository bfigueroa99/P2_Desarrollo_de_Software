# Generated by Django 4.2.5 on 2023-09-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_respuesta_tema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='BackEnd/media')),
            ],
        ),
    ]
