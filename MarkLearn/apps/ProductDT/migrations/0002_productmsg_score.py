# Generated by Django 2.0.7 on 2018-09-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductDT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmsg',
            name='score',
            field=models.IntegerField(default=1, verbose_name='综合评分'),
            preserve_default=False,
        ),
    ]
