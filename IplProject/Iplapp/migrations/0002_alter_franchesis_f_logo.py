# Generated by Django 4.2.5 on 2024-02-01 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iplapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchesis',
            name='f_logo',
            field=models.ImageField(blank=True, null=True, upload_to='franchesis_logo/'),
        ),
    ]
