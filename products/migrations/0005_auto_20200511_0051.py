# Generated by Django 3.0.1 on 2020-05-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200511_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
