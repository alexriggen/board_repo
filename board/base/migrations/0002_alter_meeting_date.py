# Generated by Django 5.0.1 on 2024-03-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
