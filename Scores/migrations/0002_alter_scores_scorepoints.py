# Generated by Django 3.2.2 on 2021-07-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='ScorePoints',
            field=models.IntegerField(),
        ),
    ]
