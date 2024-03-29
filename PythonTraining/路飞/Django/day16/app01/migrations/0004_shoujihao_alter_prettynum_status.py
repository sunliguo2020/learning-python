# Generated by Django 4.1.3 on 2022-12-04 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_prettynum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoujihao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROD_INST_ID', models.CharField(max_length=255)),
                ('CUST_ID', models.CharField(max_length=255)),
                ('LATN', models.CharField(max_length=255, verbose_name='区号')),
                ('BUSI_NBR', models.CharField(max_length=255)),
                ('USER_NAME', models.CharField(max_length=255)),
                ('CUST_NAME', models.CharField(max_length=255)),
                ('INSTALL_ADDR', models.CharField(max_length=255, verbose_name='安装地址')),
                ('CERTIFICATES_NBR', models.CharField(max_length=255, verbose_name='身份证号')),
                ('mod_time', models.DateTimeField(verbose_name='修改时间')),
            ],
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已占用'), (2, '未占用')], default=2, verbose_name='状态'),
        ),
    ]
