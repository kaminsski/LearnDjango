# Generated by Django 4.2.6 on 2023-11-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlagApp', '0010_records1'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='createdAt',
            field=models.DateTimeField(null=True, verbose_name='createdAt'),
        ),
        migrations.AddField(
            model_name='records1',
            name='createdAt',
            field=models.DateTimeField(null=True, verbose_name='createdAt'),
        ),
    ]