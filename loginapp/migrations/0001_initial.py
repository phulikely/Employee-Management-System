# Generated by Django 3.1.7 on 2021-03-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('pwd', models.CharField(max_length=32)),
                ('repwd', models.CharField(max_length=32)),
            ],
        ),
    ]