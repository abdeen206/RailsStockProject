# Generated by Django 2.2.6 on 2019-10-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_profile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
