# Generated by Django 2.2.7 on 2021-06-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parachapp', '0003_auto_20210623_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='files',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]