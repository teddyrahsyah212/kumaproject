# Generated by Django 2.2 on 2021-02-11 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=500, max_length=150, upload_to='media/home/', width_field=500)),
                ('description', models.TextField()),
            ],
        ),
    ]
