# Generated by Django 5.0.4 on 2024-04-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='010999999999', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='street',
            field=models.CharField(default='khaled', max_length=50),
            preserve_default=False,
        ),
    ]
