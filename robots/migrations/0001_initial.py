# Generated by Django 5.1.4 on 2024-12-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=2)),
                ('version', models.CharField(max_length=2)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
