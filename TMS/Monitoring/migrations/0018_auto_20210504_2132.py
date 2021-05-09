# Generated by Django 3.2 on 2021-05-04 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Monitoring', '0017_auto_20210504_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='region',
            name='continent',
            field=models.PositiveIntegerField(choices=[(3, 'Africa'), (2, 'South America'), (5, 'Oceania'), (6, 'Antarctica'), (4, 'Asia'), (7, 'Unspecified'), (0, 'Europe'), (1, 'North America')], default=7),
        ),
    ]