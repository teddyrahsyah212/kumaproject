# Generated by Django 2.2 on 2021-02-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_homepagecontent_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagecontent',
            name='detail',
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
