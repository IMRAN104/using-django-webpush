# Generated by Django 3.1.1 on 2020-09-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
