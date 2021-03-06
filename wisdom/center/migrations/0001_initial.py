# Generated by Django 3.1.6 on 2021-02-09 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('course_units', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='center.course')),
            ],
        ),
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tution', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='center.course')),
            ],
        ),
        migrations.CreateModel(
            name='TeachersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_pic', models.ImageField(height_field=300, null=True, upload_to='', width_field=300)),
                ('name', models.CharField(max_length=30)),
                ('reg_nummber', models.CharField(max_length=50)),
                ('teacher_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.course')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherAttendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='center.course')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teachersname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='center.teachersdetail')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_pic', models.ImageField(height_field=300, null=True, upload_to='', width_field=300)),
                ('name', models.CharField(max_length=30)),
                ('date_birth', models.DateField()),
                ('reg_nummber', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='center.course')),
                ('fees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.tuition')),
            ],
        ),
    ]
