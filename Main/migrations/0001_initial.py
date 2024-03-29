# Generated by Django 2.2.3 on 2019-08-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LostItems',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('managementID', models.CharField(blank=True, db_column='managementID', max_length=100, null=True)),
                ('findYmd', models.CharField(blank=True, db_column='findYmd', max_length=100, null=True)),
                ('productName', models.CharField(blank=True, db_column='productName', max_length=100, null=True)),
                ('keepPlace', models.CharField(blank=True, db_column='keepPlace', max_length=100, null=True)),
                ('productImg', models.CharField(blank=True, db_column='productImg', max_length=100, null=True)),
                ('productDesc', models.CharField(blank=True, db_column='productDesc', max_length=200, null=True)),
                ('productClass', models.CharField(blank=True, db_column='productClass', max_length=100, null=True)),
                ('placeAddress', models.CharField(blank=True, db_column='placeAddress', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LostItemsTemp',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('managementID', models.CharField(blank=True, db_column='managementID', max_length=100, null=True)),
                ('findYmd', models.CharField(blank=True, db_column='findYmd', max_length=100, null=True)),
                ('productName', models.CharField(blank=True, db_column='productName', max_length=100, null=True)),
                ('keepPlace', models.CharField(blank=True, db_column='keepPlace', max_length=100, null=True)),
                ('productImg', models.CharField(blank=True, db_column='productImg', max_length=100, null=True)),
                ('productDesc', models.CharField(blank=True, db_column='productDesc', max_length=200, null=True)),
                ('productClass', models.CharField(blank=True, db_column='productClass', max_length=100, null=True)),
                ('placeAddress', models.CharField(blank=True, db_column='placeAddress', max_length=100, null=True)),
            ],
        ),
    ]
