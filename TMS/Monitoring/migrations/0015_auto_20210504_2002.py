# Generated by Django 3.2 on 2021-05-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0014_auto_20210502_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='hour',
            field=models.CharField(choices=[('6:00', '6:00'), ('6:30', '6:30'), ('7:00', '7:00'), ('7:30', '7:30'), ('8:00', '8:00'), ('8:30', '8:30')], max_length=32),
        ),
        migrations.AlterField(
            model_name='region',
            name='continent',
            field=models.PositiveIntegerField(choices=[(5, 'Oceania'), (2, 'South America'), (6, 'Antarctica'), (0, 'Europe'), (4, 'Asia'), (3, 'Africa'), (1, 'North America'), (7, 'Unspecified')], default=7),
        ),
    ]
