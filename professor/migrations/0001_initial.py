# Generated by Django 2.2.5 on 2019-09-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('idade', models.IntegerField(verbose_name='idade')),
            ],
        ),
    ]
