# Generated by Django 4.2.6 on 2023-11-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='userLastNumber',
            field=models.IntegerField(null=True, verbose_name='User Last Number'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='userListeElemani',
            field=models.IntegerField(null=True, verbose_name='User Liste Elemanı'),
        ),
    ]
