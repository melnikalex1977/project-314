# Generated by Django 3.2.4 on 2021-10-18 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_proba_product1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Cart1',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='CartItem1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
                ('product1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product1')),
            ],
            options={
                'db_table': 'CartItem1',
            },
        ),
    ]
