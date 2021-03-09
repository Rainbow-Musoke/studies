# Generated by Django 3.1.6 on 2021-02-09 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
        ('students', '0002_assingmenthandin_handin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assingmenthandin',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='center.course'),
        ),
        migrations.AlterField(
            model_name='assingmenthandin',
            name='course_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='center.units'),
        ),
    ]