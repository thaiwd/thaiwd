# Generated by Django 3.2.7 on 2021-09-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoadminuser',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
