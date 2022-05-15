# Generated by Django 4.0.1 on 2022-05-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_delete_contact_delete_newslatter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Done')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Newslatter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
    ]
