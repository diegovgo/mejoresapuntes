# Generated by Django 2.2.5 on 2020-04-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityconnection', '0012_auto_20200430_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_picture',
            field=models.ImageField(default='user/profile_picture/nophoto.jpg', upload_to='users/profile_picture'),
        ),
    ]