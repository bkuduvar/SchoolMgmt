# Generated by Django 3.0.7 on 2021-02-01 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_ID', models.CharField(default=' ', max_length=10, primary_key=True, serialize=False)),
                ('school_name', models.CharField(default='', max_length=50, null=True)),
                ('school_street_address', models.CharField(default='', max_length=100, null=True)),
                ('school_city', models.CharField(default='', max_length=50, null=True)),
                ('school_state', models.CharField(default='', max_length=50, null=True)),
                ('school_zip', models.CharField(blank=True, default='00000', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_ID', models.CharField(default=' ', max_length=10, primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(default='', max_length=50, null=True)),
                ('teaching_grade', models.CharField(default='', max_length=50, null=True)),
                ('teacher_street_address', models.CharField(default='', max_length=100, null=True)),
                ('teacher_city', models.CharField(default='', max_length=50, null=True)),
                ('teacher_state', models.CharField(default='', max_length=50, null=True)),
                ('teacher_zip', models.CharField(blank=True, default='00000', max_length=50, null=True)),
                ('school_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='Schools.School')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_ID', models.CharField(default=' ', max_length=10, primary_key=True, serialize=False)),
                ('student_lastname', models.CharField(default='', max_length=50, null=True)),
                ('student_firstname', models.CharField(default='', max_length=50, null=True)),
                ('student_grade', models.CharField(default='', max_length=50, null=True)),
                ('student_school_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='School', to='Schools.School')),
                ('student_teacher_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teacher', to='Schools.Teacher')),
            ],
        ),
    ]
