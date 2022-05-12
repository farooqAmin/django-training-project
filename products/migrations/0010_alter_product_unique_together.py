# Generated by Django 4.0.4 on 2022-05-10 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_address_user_alter_userprofile_address'),
        ('products', '0009_alter_product_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'vendor', 'sub_category')},
        ),
    ]
