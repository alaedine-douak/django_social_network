# Generated by Django 3.1.4 on 2020-12-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201206_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/avatar.png', upload_to='avatars/'),
        ),
    ]