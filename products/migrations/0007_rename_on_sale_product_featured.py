# Generated by Django 3.2.16 on 2023-02-12 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_on_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='on_sale',
            new_name='featured',
        ),
    ]
