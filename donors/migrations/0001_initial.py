# Generated by Django 3.0.1 on 2020-01-07 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Required', max_length=50)),
                ('last_name', models.CharField(default='Required', max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.IntegerField(default=1234567890)),
                ('cc_num', models.IntegerField(default=123412412341234)),
                ('ccv_num', models.IntegerField(default=0)),
                ('cc_expiration', models.CharField(default='MM/YYYY', max_length=10)),
            ],
        ),
    ]