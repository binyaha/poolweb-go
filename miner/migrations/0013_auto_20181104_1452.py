# Generated by Django 2.1.1 on 2018-11-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miner', '0012_miner_pool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miner',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
