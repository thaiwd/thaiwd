# Generated by Django 3.2.7 on 2021-09-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_infoadminuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoadminuser',
            name='introduce2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='infoadminuser',
            name='introduce3',
            field=models.TextField(blank=True),
        ),
    ]
