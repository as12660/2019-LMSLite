# Generated by Django 2.1.7 on 2019-04-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20190416_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='average',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
