# Generated by Django 5.0 on 2023-12-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_finishedbuilding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finishedbuilding',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='finishedbuilding',
            name='start_date',
            field=models.DateField(),
        ),
    ]
