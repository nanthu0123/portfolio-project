# Generated by Django 3.0.3 on 2020-02-26 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200225_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='user_image',
            new_name='image',
        ),
    ]
