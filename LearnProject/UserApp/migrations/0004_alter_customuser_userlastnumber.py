# Generated by Django 4.2.6 on 2023-11-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_listeelemaniuser_remove_customuser_userlisteelemani_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userLastNumber',
            field=models.IntegerField(blank=True, null=True, verbose_name='User Last Number'),
        ),
    ]