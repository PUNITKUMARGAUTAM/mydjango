# Generated by Django 3.2.6 on 2021-08-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentrollno', models.CharField(max_length=300)),
                ('studentname', models.CharField(max_length=50)),
                ('studentbranch', models.CharField(max_length=50)),
                ('studentdpt', models.CharField(max_length=50)),
            ],
        ),
    ]