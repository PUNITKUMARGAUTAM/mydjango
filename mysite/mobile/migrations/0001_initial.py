# Generated by Django 3.2.6 on 2021-08-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilesplus', models.CharField(max_length=300)),
                ('mobilesrealme', models.CharField(max_length=50)),
                ('mobilesredmi', models.CharField(max_length=50)),
                ('mobilesapple', models.CharField(max_length=50)),
            ],
        ),
    ]
