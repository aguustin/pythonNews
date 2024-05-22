# Generated by Django 5.0.2 on 2024-05-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FileField(upload_to='users_profiles')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('userType', models.IntegerField()),
            ],
            options={
                'db_table': 'Users',
                'ordering': ['id'],
            },
        ),
    ]
