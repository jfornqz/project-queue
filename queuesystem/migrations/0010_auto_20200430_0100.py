# Generated by Django 2.2.2 on 2020-04-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queuesystem', '0009_queue_system_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue_system',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
