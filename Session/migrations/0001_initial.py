# Generated by Django 3.2.2 on 2021-07-11 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExeercisePlan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfCreation', models.DateTimeField(blank=True, null=True)),
                ('Session_Plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_plan', to='ExeercisePlan.exercise_plan')),
            ],
        ),
    ]
