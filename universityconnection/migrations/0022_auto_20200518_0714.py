# Generated by Django 2.2.5 on 2020-05-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityconnection', '0021_auto_20200518_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='career',
            field=models.ManyToManyField(blank=True, null=True, related_name='myuser', to='universityconnection.Career'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, related_name='myuser', to='universityconnection.Course'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='university',
            field=models.ManyToManyField(blank=True, null=True, related_name='myuser', to='universityconnection.University'),
        ),
    ]
