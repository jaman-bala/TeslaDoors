# Generated by Django 3.2.9 on 2023-04-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_product_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='adress',
            field=models.CharField(max_length=10, verbose_name='Адрес'),
        ),
    ]