# Generated by Django 5.0.2 on 2024-05-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.FileField(blank=True, null=True, upload_to='users_profiles'),
        ),
    ]
