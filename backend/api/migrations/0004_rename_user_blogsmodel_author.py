# Generated by Django 4.1 on 2022-09-01 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_blogsmodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogsmodel',
            old_name='user',
            new_name='author',
        ),
    ]
