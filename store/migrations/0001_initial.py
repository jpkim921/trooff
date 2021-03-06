# Generated by Django 3.0.1 on 2020-05-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(choices=[('Cup', 'Cup'), ('Plate', 'Plate'), ('Bowl', 'Bowl'), ('Vase', 'Vase')], max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('tags', models.ManyToManyField(to='store.Tag')),
            ],
        ),
    ]
