# Generated by Django 4.1 on 2023-08-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=1, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
