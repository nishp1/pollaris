# Generated by Django 2.2.6 on 2019-12-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0002_lat_long_type")]

    operations = [
        migrations.AlterField(
            model_name="dropboxlocation",
            name="location_id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="earlyvotelocation",
            name="location_id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="pollinglocation",
            name="location_id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
