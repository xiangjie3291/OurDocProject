# Generated by Django 3.0.8 on 2020-08-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_account', models.CharField(max_length=16)),
                ('user_password', models.CharField(max_length=16)),
                ('user_nickname', models.CharField(max_length=16)),
                ('user_icon', models.URLField()),
            ],
        ),
    ]
