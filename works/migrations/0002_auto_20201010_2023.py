# Generated by Django 2.2.2 on 2020-10-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='img'),
        ),
    ]
