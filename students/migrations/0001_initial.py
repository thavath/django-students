# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-08 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attendace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_study', models.DateField()),
                ('status', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_peroid_of_working', models.DateField(blank=True)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('job', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fujiyama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField()),
                ('score', models.FloatField(default=0)),
                ('player_learn_detail', models.CharField(max_length=200)),
                ('correct_answer', models.IntegerField(default=0)),
                ('duration', models.DurationField()),
                ('email', models.EmailField(max_length=250)),
                ('incorrect_answer', models.IntegerField(default=0)),
                ('login_source', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateField(blank=True)),
                ('interview_type', models.CharField(blank=True, max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('job_history', models.CharField(blank=True, max_length=200)),
                ('certificate', models.CharField(blank=True, max_length=200)),
                ('certificate_file', models.FileField(blank=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=200)),
                ('khmer_name', models.CharField(blank=True, max_length=200)),
                ('japanese_name', models.CharField(blank=True, max_length=200)),
                ('nationality', models.CharField(max_length=50)),
                ('place_of_birth', models.CharField(max_length=200)),
                ('card_id', models.CharField(blank=True, max_length=100)),
                ('khmer_salary', models.FloatField(blank=True, max_length=10)),
                ('education', models.CharField(choices=[(b'Primary School', b'Primary School'), (b'Secondary School', b'Secondary School'), (b'High School', b'High School'), (b'University', b'University'), (b'Vocation School', b'Vocation Shool'), (b'Traning School', b'Traning School')], max_length=200)),
                ('date_of_birth', models.DateField()),
                ('age', models.PositiveIntegerField(default=False)),
                ('gender', models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female')], max_length=200)),
                ('state_of_healt', models.CharField(blank=True, max_length=20)),
                ('blood_type', models.CharField(blank=True, max_length=20)),
                ('vision', models.CharField(blank=True, max_length=50)),
                ('interest', models.CharField(blank=True, max_length=50)),
                ('year_of_experience', models.IntegerField(default=0)),
                ('married', models.CharField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], max_length=50)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('behavior', models.CharField(blank=True, max_length=50)),
                ('went_to_japan', models.CharField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], max_length=50)),
                ('japanese_conversation', models.CharField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], max_length=50)),
                ('height', models.CharField(blank=True, max_length=50)),
                ('weight', models.CharField(blank=True, max_length=50)),
                ('current_address', models.CharField(max_length=200)),
                ('reason', models.TextField(choices=[(b'Increase Revenue', b'Increase Revenue'), (b'Respect to parents', b'Respect to parents'), (b'Improve Living', b'Improve Living'), (b'Education', b'Education'), (b'Other Reason', b'Other Reason')], max_length=255)),
                ('arrang_money', models.TextField(blank=True, max_length=255)),
                ('sending_company', models.CharField(choices=[(b'Company 168', b'Company 168'), (b'Phnom Penh Thmey', b'Phnom Penh Thmey'), (b'CL Supply Company', b'CL Supply COMPANY'), (b'Other Company', b'Other Company')], max_length=200)),
                ('japanese_level', models.CharField(choices=[(b'level', b'level'), (b'N5', b'N5'), (b'N4', b'N4'), (b'N3', b'N3'), (b'N2', b'N2'), (b'N1', b'N1')], max_length=50)),
                ('field_of_work', models.CharField(blank=True, max_length=50)),
                ('date_go_japan', models.DateField(blank=True)),
                ('prefecture', models.CharField(blank=True, max_length=50)),
                ('zip_code', models.CharField(blank=True, max_length=50)),
                ('address_in_japan', models.CharField(max_length=200)),
                ('grammer_level', models.CharField(blank=True, max_length=200)),
                ('idiom_level', models.CharField(blank=True, max_length=200)),
                ('conversation_level', models.CharField(blank=True, max_length=200)),
                ('life_attitude', models.CharField(blank=True, max_length=200)),
                ('course_type', models.CharField(blank=True, max_length=100)),
                ('last_peroid_of_study', models.DateField(blank=True)),
                ('university_name', models.CharField(blank=True, max_length=200)),
                ('subject_name', models.CharField(blank=True, max_length=100)),
                ('teacher_name', models.CharField(blank=True, max_length=50)),
                ('book_type', models.CharField(blank=True, max_length=50)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('admin', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
        migrations.AddField(
            model_name='fujiyama',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
        migrations.AddField(
            model_name='family',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
        migrations.AddField(
            model_name='experience',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
        migrations.AddField(
            model_name='attendace',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
        migrations.AddField(
            model_name='academic',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]
