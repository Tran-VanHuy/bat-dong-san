# Generated by Django 5.0.1 on 2024-01-17 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0007_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='link',
            field=models.TextField(default='#'),
        ),
    ]
