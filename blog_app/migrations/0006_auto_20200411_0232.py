# Generated by Django 3.0.3 on 2020-04-11 00:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20200411_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogBody',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Body'),
        ),
    ]