# Generated by Django 4.1 on 2022-08-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('parentesco', models.CharField(max_length=64)),
                ('fecha_nacimiento', models.DateField()),
                ('cant_patas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
