# Generated by Django 2.2.2 on 2019-08-05 05:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_length_years', models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(choices=[('Unit 1', 'Unit Test 1'), ('Unit 2', 'Unit Test 2'), ('Lab 1', 'Lab Test 1'), ('Lab 2', 'Lab Test 2'), ('Final', 'Final Test')], max_length=10)),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.Class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('students', models.ManyToManyField(to='SoMPortal.StudentProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st sem', '1st Semester'), ('2nd sem', '2nd Semester'), ('3rd sem', '3rd Semester'), ('4th sem', '4th Semester'), ('5th sem', '5th Semester'), ('6th sem', '6th Semester'), ('7th sem', '7th Semester'), ('8th sem', '8th Semester')], max_length=12)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.Class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoMPortal.StudentProfile')),
                ('test', models.ManyToManyField(to='SoMPortal.Test')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(blank=True, to='SoMPortal.StudentProfile'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ManyToManyField(blank=True, to='SoMPortal.TeacherProfile'),
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
