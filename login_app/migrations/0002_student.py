# Generated by Django 4.1.3 on 2022-11-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_ID', models.IntegerField()),
                ('S_NAME', models.CharField(max_length=70)),
                ('S_EMAIL', models.CharField(max_length=70)),
                ('S_PASS', models.CharField(max_length=40)),
            ],
        ),
    ]