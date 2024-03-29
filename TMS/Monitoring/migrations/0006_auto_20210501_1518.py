# Generated by Django 3.2 on 2021-05-01 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0005_auto_20210501_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='region',
        ),
        migrations.AlterField(
            model_name='region',
            name='continent',
            field=models.PositiveIntegerField(choices=[(7, 'Unspecified'), (4, 'Asia'), (6, 'Antarctica'), (2, 'South America'), (5, 'Oceania'), (3, 'Africa'), (1, 'North America'), (0, 'Europe')], default=7),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('short_name', models.CharField(max_length=64)),
                ('region', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Monitoring.region')),
            ],
        ),
        migrations.AlterField(
            model_name='supplier',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monitoring.country'),
        ),
    ]
