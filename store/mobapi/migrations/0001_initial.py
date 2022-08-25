# Generated by Django 4.1 on 2022-08-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('colour', models.CharField(max_length=20)),
                ('cc', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=30)),
            ],
        ),
    ]