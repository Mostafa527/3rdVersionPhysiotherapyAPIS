# Generated by Django 3.2.2 on 2021-05-13 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clinic', '0001_initial'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physiotherapist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='physio_user', serialize=False, to='Accounts.newuser')),
                ('Clinic_Physio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pysio_therpists', to='Clinic.clinic')),
            ],
        ),
    ]
