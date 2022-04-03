# Generated by Django 2.2.26 on 2022-04-03 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_id', models.BigIntegerField()),
                ('plan_id', models.BigIntegerField()),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
