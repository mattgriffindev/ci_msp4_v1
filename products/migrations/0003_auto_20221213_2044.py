# Generated by Django 3.2.16 on 2022-12-13 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image1_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
