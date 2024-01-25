# Generated by Django 5.0.1 on 2024-01-23 15:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ImageField(upload_to='uploads/product/')),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('last_change', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('address', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('status', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.costumer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]