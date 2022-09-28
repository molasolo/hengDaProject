# Generated by Django 4.1.1 on 2022-09-28 06:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=' 产品标题')),
                ('description', models.TextField(verbose_name='产品详情描述')),
                ('productType', models.CharField(choices=[('家用机器人', '家用机器人'), ('智能监控', '智能监控'), ('人脸识别解决方案', '人脸识别解决方案')], max_length=50, verbose_name='产品类型')),
                ('price', models.DecimalField(decimal_places=1, max_digits=7, null=True, verbose_name='产品价格')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'ordering': ('-publishDate',),
            },
        ),
        migrations.CreateModel(
            name='ProductImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='Product/', verbose_name='产品图片')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productImgs', to='productsApp.product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '产品图片',
                'verbose_name_plural': '产品图片',
            },
        ),
    ]
