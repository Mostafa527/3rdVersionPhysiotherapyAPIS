# Generated by Django 3.2.2 on 2021-07-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExeercisePlan', '0002_auto_20210706_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise_plan',
            name='DateOfEnd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercise_plan',
            name='DateOfStart',
            field=models.DateField(blank=True, null=True),
        ),
    ]