# Generated by Django 3.2.9 on 2023-04-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20230410_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sum_currency',
        ),
        migrations.AlterField(
            model_name='product',
            name='sum',
            field=models.CharField(max_length=10, verbose_name='Сумма'),
        ),
    ]
