# Generated by Django 4.2.6 on 2023-11-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlagApp', '0006_delete_lastnumber_delete_listeelemani'),
    ]

    operations = [
        migrations.AddField(
            model_name='flagmodel',
            name='flagPoint',
            field=models.IntegerField(null=True, verbose_name='Flag Point'),
        ),
    ]