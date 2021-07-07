# Generated by Django 3.2.2 on 2021-07-06 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ExeercisePlan', '0003_auto_20210706_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise_plan',
            name='DateOfEnd',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exercise_plan',
            name='DateOfStart',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]