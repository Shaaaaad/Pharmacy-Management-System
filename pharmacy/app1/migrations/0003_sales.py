# Generated by Django 4.2.6 on 2023-11-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('medicinename', models.CharField(max_length=50)),
                ('medicineqty', models.CharField(max_length=50)),
            ],
        ),
    ]
