# Generated by Django 3.0.3 on 2020-04-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceLink', models.URLField(max_length=500)),
                ('title', models.CharField(max_length=50)),
                ('featuredImage', models.ImageField(upload_to='images')),
                ('minister', models.CharField(max_length=70)),
            ],
        ),
    ]
