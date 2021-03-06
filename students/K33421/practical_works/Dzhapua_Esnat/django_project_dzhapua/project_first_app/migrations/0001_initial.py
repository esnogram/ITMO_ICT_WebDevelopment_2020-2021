# Generated by Django 3.1.2 on 2021-01-12 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('number', models.CharField(max_length=15)),
                ('mark', models.CharField(max_length=20)),
                ('carmodel', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Carowner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('lastname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('birthday', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('carowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('licnumber', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('carowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
    ]
