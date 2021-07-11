# Generated by Django 3.2.2 on 2021-07-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, unique=True)),
                ('Address', models.CharField(max_length=300)),
                ('Contact', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=150, unique=True)),
            ],
        ),
    ]
