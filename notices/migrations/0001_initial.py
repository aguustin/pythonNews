# Generated by Django 5.0.2 on 2024-05-23 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Category',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=200)),
                ('imageTitle', models.FileField(upload_to='news_images')),
                ('firsParagraph', models.TextField()),
                ('secondParagraph', models.TextField()),
                ('thirdParagraph', models.TextField()),
                ('firstImage', models.FileField(upload_to='news_images')),
                ('secondImage', models.FileField(upload_to='news_images')),
                ('thirdImage', models.FileField(upload_to='news_images')),
            ],
            options={
                'db_table': 'News',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Category_New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='notices.category')),
                ('new_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='notices.new')),
            ],
            options={
                'db_table': 'Categories_and_News',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User_New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='notices.new')),
                ('user_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'User_New',
                'ordering': ['id'],
            },
        ),
    ]
