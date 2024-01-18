# Generated by Django 5.0.1 on 2024-01-18 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0018_review_infoproject_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoproject',
            name='review',
        ),
        migrations.CreateModel(
            name='InfoReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('svg', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_results', to='ui.review')),
            ],
        ),
    ]