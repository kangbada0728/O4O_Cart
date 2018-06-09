# Generated by Django 2.0.5 on 2018-06-09 13:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img_Selector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='시작날짜')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='마지막날짜')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info', verbose_name='고객')),
            ],
            options={
                'verbose_name': '이미지 선택기',
                'verbose_name_plural': '이미지 선택기',
            },
        ),
    ]
