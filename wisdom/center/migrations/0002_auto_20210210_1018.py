# Generated by Django 3.1.6 on 2021-02-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsdetail',
            name='student_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='teachersdetail',
            name='teacher_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
