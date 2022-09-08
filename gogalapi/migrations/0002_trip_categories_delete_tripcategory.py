# Generated by Django 4.1 on 2022-09-07 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gogalapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='categories',
            field=models.ManyToManyField(related_name='trips', to='gogalapi.category'),
        ),
        migrations.DeleteModel(
            name='TripCategory',
        ),
    ]