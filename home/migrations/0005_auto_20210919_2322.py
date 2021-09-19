# Generated by Django 3.2.7 on 2021-09-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_infoadminuser_infoadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('introduce', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='InfoAdmin',
        ),
    ]