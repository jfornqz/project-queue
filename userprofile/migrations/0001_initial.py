# Generated by Django 2.2.2 on 2020-04-23 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='medical_history',
            fields=[
                ('occupation', models.CharField(max_length=255)),
                ('congenital_disease', models.CharField(max_length=255)),
                ('fname_emergency', models.CharField(max_length=255)),
                ('lname_emergency', models.CharField(max_length=255)),
                ('address_emergency', models.TextField()),
                ('relationship_emergency', models.CharField(max_length=255)),
                ('phone_emergency', models.CharField(max_length=10)),
                ('account_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='admission_note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.IntegerField()),
                ('patient_types', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('drug_allergic', models.CharField(max_length=255)),
                ('symptoms', models.TextField()),
                ('create_date', models.DateField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
