# Generated by Django 5.0.1 on 2024-01-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0005_alter_member_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(unique=True, upload_to='static/images')),
                ('link', models.TextField()),
            ],
        ),
    ]
