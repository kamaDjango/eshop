# Generated by Django 4.0.1 on 2022-04-24 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='products',
        ),
        migrations.CreateModel(
            name='CheckoutProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('q', models.IntegerField(default=1)),
                ('total', models.IntegerField(default=0)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.checkout')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
    ]