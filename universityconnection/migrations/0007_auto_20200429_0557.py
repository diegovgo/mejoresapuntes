# Generated by Django 2.2.5 on 2020-04-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityconnection', '0006_file_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='link',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]