# Generated by Django 3.2.4 on 2022-07-06 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('desc', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('desc', models.TextField(max_length=1000)),
                ('course', models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.course')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=10)),
                ('start_end_time', models.CharField(max_length=50)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.course')),
            ],
        ),
    ]
