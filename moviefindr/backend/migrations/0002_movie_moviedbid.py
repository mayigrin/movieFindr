# Generated by Django 3.1.1 on 2020-09-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movieDbId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
