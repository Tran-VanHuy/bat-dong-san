# Generated by Django 5.0.1 on 2024-01-17 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0012_infoproject_project_id_remove_project_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='info',
        ),
    ]