# Generated by Django 3.0.3 on 2020-04-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20200411_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likeCount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]