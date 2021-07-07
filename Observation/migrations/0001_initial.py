# Generated by Django 3.2.2 on 2021-05-13 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
        ('Session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfCreation', models.DateTimeField()),
                ('Notes', models.CharField(max_length=300)),
                ('Patient_Observation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_observ', to='Patient.patient')),
                ('Session_Observation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_observ', to='Session.session')),
            ],
        ),
    ]
