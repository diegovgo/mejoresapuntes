# Generated by Django 2.2.5 on 2020-04-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityconnection', '0004_note_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=0, upload_to='users/pdfs'),
        ),
    ]
