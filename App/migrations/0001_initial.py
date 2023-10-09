# Generated by Django 4.2.6 on 2023-10-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='uploads')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
