# Generated by Django 5.0.1 on 2024-01-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduce',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]