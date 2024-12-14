# Generated by Django 5.1.4 on 2024-12-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('room_type', models.CharField(choices=[('SINGLE', 'Single'), ('DOUBLE', 'Double'), ('SUITE', 'Suite')], max_length=10)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]