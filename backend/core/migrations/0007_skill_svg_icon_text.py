# Generated by Django 4.1.7 on 2024-03-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_project_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='svg_icon_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
