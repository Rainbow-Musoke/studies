# Generated by Django 3.1.6 on 2021-02-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assingmenthandin',
            name='handin',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
