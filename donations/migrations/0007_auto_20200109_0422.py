# Generated by Django 3.0.1 on 2020-01-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0006_auto_20200109_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='cc_expiration',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='cc_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='donor',
            name='ccv_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]