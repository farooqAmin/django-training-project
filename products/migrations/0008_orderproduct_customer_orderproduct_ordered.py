# Generated by Django 4.0.4 on 2022-05-09 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_address_user_alter_userprofile_address'),
        ('products', '0007_alter_orderproduct_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
