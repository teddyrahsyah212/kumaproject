# Generated by Django 2.2 on 2021-02-15 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20210215_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepagecontent',
            name='images',
            field=models.ImageField(default='None/no-img.jpg', max_length=150, upload_to='service/'),
        ),
    ]