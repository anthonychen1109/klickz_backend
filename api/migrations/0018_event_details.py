# Generated by Django 2.0.4 on 2018-09-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20180930_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='details',
            field=models.TextField(default=''),
        ),
    ]
