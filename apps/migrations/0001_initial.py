# Generated by Django 3.2.13 on 2022-07-29 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='applists',
            fields=[
                ('appname', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='App name')),
                ('appimg', models.ImageField(blank=True, null=True, upload_to='app_images')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
