# Generated by Django 2.2.26 on 2022-04-12 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20220410_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apps',
            old_name='subscription_id',
            new_name='subscription',
        ),
        migrations.RenameField(
            model_name='apps',
            old_name='user_id',
            new_name='user',
        ),
    ]
