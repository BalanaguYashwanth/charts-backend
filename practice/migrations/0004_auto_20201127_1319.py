# Generated by Django 3.1.1 on 2020-11-27 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_auto_20201127_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addition',
            old_name='timstamp',
            new_name='timestamp',
        ),
    ]