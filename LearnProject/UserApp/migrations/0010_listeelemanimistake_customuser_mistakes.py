# Generated by Django 4.2.6 on 2023-11-26 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0009_customuser_gamepoint1_customuser_userlastnumber1'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeElemaniMistake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userListeElemaniMany', models.IntegerField(null=True, verbose_name='Many')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='mistakes',
            field=models.ManyToManyField(to='UserApp.listeelemanimistake', verbose_name='Mistakes'),
        ),
    ]
