# Generated by Django 5.1.2 on 2024-12-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Phone'),
        ),
    ]
