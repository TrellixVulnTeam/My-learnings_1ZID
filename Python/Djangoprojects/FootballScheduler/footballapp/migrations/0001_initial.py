# Generated by Django 2.0 on 2020-05-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamName', models.CharField(max_length=100)),
                ('Player1', models.CharField(max_length=100)),
                ('Player2', models.CharField(max_length=100)),
                ('Player3', models.CharField(max_length=100)),
                ('Player4', models.CharField(max_length=100)),
                ('Player5', models.CharField(max_length=100)),
                ('Player6', models.CharField(max_length=100)),
                ('Player7', models.CharField(max_length=100)),
                ('Player8', models.CharField(max_length=100)),
                ('Player9', models.CharField(max_length=100)),
                ('Player10', models.CharField(max_length=100)),
                ('Player11', models.CharField(max_length=100)),
                ('Coach', models.CharField(max_length=100)),
                ('Manager1', models.CharField(max_length=100)),
                ('Manager2', models.CharField(max_length=100)),
            ],
        ),
    ]
