# Generated by Django 2.2 on 2021-02-11 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210211_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicepageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicepageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='None/no-img.jpg', max_length=150, upload_to='service/img/')),
                ('icon', models.ImageField(default='None/no-img.jpg', max_length=150, upload_to='service/icon/')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ServicepageContent')),
            ],
        ),
    ]
