# Generated by Django 2.2.5 on 2020-05-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityconnection', '0016_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]