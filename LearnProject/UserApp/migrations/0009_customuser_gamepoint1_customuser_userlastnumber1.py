# Generated by Django 4.2.6 on 2023-11-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0008_listeelemaniuser1_customuser_userlisteelemani1'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gamePoint1',
            field=models.IntegerField(blank=True, default=0, verbose_name='Game Point'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='userLastNumber1',
            field=models.IntegerField(blank=True, null=True, verbose_name='User Last Number'),
        ),
    ]