# Generated by Django 3.1.1 on 2020-10-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=90)),
                ('department_name', models.CharField(max_length=90)),
            ],
        ),
    ]
