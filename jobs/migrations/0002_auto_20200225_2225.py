# Generated by Django 3.0.3 on 2020-02-26 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='user_image',
        ),
    ]
