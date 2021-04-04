# Generated by Django 2.0.2 on 2021-04-04 14:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210404_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='weekdays',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=13),
        ),
    ]
