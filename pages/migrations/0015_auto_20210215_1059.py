# Generated by Django 2.2 on 2021-02-15 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20210215_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepagecontent',
            name='tab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='pages.ServicepageTab'),
        ),
    ]
