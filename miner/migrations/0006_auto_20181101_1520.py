# Generated by Django 2.1.1 on 2018-11-01 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miner', '0005_miner_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poolmux',
            name='miner',
        ),
        migrations.RemoveField(
            model_name='poolmux',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='miner',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Pool',
        ),
        migrations.DeleteModel(
            name='PoolMux',
        ),
    ]
