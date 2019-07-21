# Generated by Django 2.2.2 on 2019-07-19 01:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SoMPortal', '0002_class_course_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(choices=[('Unit', 'Unit Test'), ('Lab', 'Lab Test'), ('Final', 'Final Test')], max_length=10)),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.Class')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester')], max_length=12)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.Class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.Student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.Test')),
            ],
        ),
    ]