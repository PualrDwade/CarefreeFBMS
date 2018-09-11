# Generated by Django 2.0.7 on 2018-09-10 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TraverMsg', '0003_auto_20180909_2359'),
        ('ProductDT', '0007_auto_20180909_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrategyMsg',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='攻略id')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('link_url', models.CharField(max_length=100, verbose_name='攻略链接')),
                ('simple_content', models.CharField(max_length=1000, verbose_name='简介')),
                ('img_url', models.CharField(max_length=100, verbose_name='图片链接')),
                ('city_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TraverMsg.CityMsg', verbose_name='相关城市')),
                ('scenic_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TraverMsg.ScenicMsg', verbose_name='相关景点')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductDT.Supplier', verbose_name='供应商')),
            ],
            options={
                'verbose_name': '攻略信息',
            },
        ),
        migrations.RemoveField(
            model_name='ticketsmsg',
            name='ticket_num',
        ),
        migrations.AddField(
            model_name='ticketsmsg',
            name='scense_address',
            field=models.CharField(max_length=100, null=True, verbose_name='场景地址'),
        ),
        migrations.AlterField(
            model_name='ticketsmsg',
            name='scenic_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TraverMsg.ScenicMsg', verbose_name='所属景点'),
        ),
        migrations.AlterField(
            model_name='ticketsmsg',
            name='supplier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductDT.Supplier', verbose_name='所属供应商'),
        ),
        migrations.AlterField(
            model_name='ticketsmsg',
            name='ticket_content',
            field=models.CharField(max_length=3000, null=True, verbose_name='费用说明'),
        ),
        migrations.AlterField(
            model_name='ticketsmsg',
            name='ticket_price',
            field=models.CharField(max_length=10, null=True, verbose_name='门票价格'),
        ),
    ]
