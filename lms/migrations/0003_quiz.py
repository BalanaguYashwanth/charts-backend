# Generated by Django 3.1.1 on 2020-11-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_auto_20201116_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.TextField()),
                ('a', models.TextField()),
                ('b', models.TextField()),
                ('c', models.TextField()),
                ('d', models.TextField()),
            ],
        ),
    ]
