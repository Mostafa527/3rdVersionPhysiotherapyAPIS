# Generated by Django 3.2.2 on 2021-05-13 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
        ('Game', '0001_initial'),
        ('Physiotherapist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfStart', models.DateField()),
                ('DateOfEnd', models.DateField()),
                ('Duration', models.FloatField()),
                ('RestTime', models.FloatField()),
                ('RepitionNum', models.IntegerField()),
                ('MembersToUse', models.IntegerField()),
                ('Difficulty', models.IntegerField()),
                ('Notes', models.CharField(max_length=500)),
                ('Game_Exerplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Game_Plan', to='Game.game')),
                ('Patient_Exerplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Patient_Plan', to='Patient.patient')),
                ('Physio_Exerplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Physio_Plan', to='Physiotherapist.physiotherapist')),
            ],
        ),
    ]
