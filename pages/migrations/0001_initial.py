# Generated by Django 4.2.4 on 2023-08-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('postalcode', models.TextField(null=True)),
                ('town', models.TextField(null=True)),
                ('provincestate', models.TextField(null=True)),
                ('nation', models.TextField(null=True)),
                ('phone', models.TextField(null=True)),
            ],
        ),
    ]
