# Generated by Django 5.0.6 on 2024-06-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]