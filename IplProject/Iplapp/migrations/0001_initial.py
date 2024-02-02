# Generated by Django 4.2.5 on 2024-02-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Franchesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('f_nickname', models.CharField(max_length=4)),
                ('f_started_year', models.IntegerField()),
                ('no_of_titles', models.IntegerField()),
                ('f_logo', models.ImageField(upload_to='franchesis_logo/')),
            ],
            options={
                'db_table': 'franchesis',
            },
        ),
    ]