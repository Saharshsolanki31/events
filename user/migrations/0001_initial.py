# Generated by Django 3.2.5 on 2021-07-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('college_name', models.CharField(max_length=200)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='static/files')),
            ],
        ),
    ]
