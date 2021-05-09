# Generated by Django 3.2 on 2021-05-04 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Monitoring', '0016_auto_20210504_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='region',
            name='continent',
            field=models.PositiveIntegerField(choices=[(6, 'Antarctica'), (3, 'Africa'), (0, 'Europe'), (7, 'Unspecified'), (5, 'Oceania'), (4, 'Asia'), (1, 'North America'), (2, 'South America')], default=7),
        ),
    ]
