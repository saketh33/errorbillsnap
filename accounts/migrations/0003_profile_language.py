# Generated by Django 3.2.13 on 2022-07-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
