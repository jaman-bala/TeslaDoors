# Generated by Django 3.2.9 on 2023-04-10 06:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20230406_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Комментарии'),
        ),
    ]