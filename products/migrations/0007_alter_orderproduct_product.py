# Generated by Django 4.0.4 on 2022-04-29 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_orderproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
