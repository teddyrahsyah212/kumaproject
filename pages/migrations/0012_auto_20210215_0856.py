# Generated by Django 2.2 on 2021-02-15 01:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20210215_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepageimage',
            name='image',
            field=models.ImageField(default='None/no-img.jpg', max_length=150, upload_to='service/', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]
