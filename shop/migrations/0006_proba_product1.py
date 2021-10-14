# Generated by Django 3.2.4 on 2021-10-14 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20211009_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='proba')),
            ],
            options={
                'verbose_name': 'proba',
                'verbose_name_plural': 'probas',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='product1')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('proba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.proba')),
            ],
            options={
                'verbose_name': 'product1',
                'verbose_name_plural': 'products1',
                'ordering': ('name',),
            },
        ),
    ]
