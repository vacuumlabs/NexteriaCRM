# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nextis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=100)),
                ('pocet_kreditov', models.IntegerField()),
                ('typ', models.CharField(choices=[('ik', 'IK'), ('dbk', 'DBK'), ('for', 'Formalna udalost'), ('ine', 'Ine')], max_length=3)),
                ('popis', models.TextField(blank=True)),
                ('kapacita', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Eventy',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('cas', models.DateTimeField(auto_now=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nextis.Student')),
            ],
            options={
                'verbose_name_plural': 'Feedbacky',
            },
        ),
        migrations.CreateModel(
            name='Miesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=200)),
                ('google_mapa', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Stretnutie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaciatok', models.DateTimeField()),
                ('koniec', models.DateTimeField()),
                ('miesto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.Miesto')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='feedbacky',
            field=models.ManyToManyField(blank=True, to='events.Feedback'),
        ),
        migrations.AddField(
            model_name='event',
            name='lektori',
            field=models.ManyToManyField(blank=True, to='nextis.Lektor'),
        ),
        migrations.AddField(
            model_name='event',
            name='levely',
            field=models.ManyToManyField(to='nextis.Level'),
        ),
        migrations.AddField(
            model_name='event',
            name='stretnutia',
            field=models.ManyToManyField(blank=True, to='events.Stretnutie'),
        ),
        migrations.AddField(
            model_name='event',
            name='ucastnici',
            field=models.ManyToManyField(blank=True, to='nextis.Student'),
        ),
    ]