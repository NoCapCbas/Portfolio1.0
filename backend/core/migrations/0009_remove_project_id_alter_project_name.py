# Generated by Django 4.1.7 on 2024-03-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_skill_id_alter_skill_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
