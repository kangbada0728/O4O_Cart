# Generated by Django 2.0.4 on 2018-05-21 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0069_auto_20180519_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_info',
            name='camera_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Camera_Info', verbose_name='카메라 번호'),
        ),
        migrations.AlterField(
            model_name='ad_info',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Items', verbose_name='구매상품'),
        ),
        migrations.AlterField(
            model_name='cart_info',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Customer_Info', verbose_name='소유자'),
        ),
        migrations.AlterField(
            model_name='coupon_item_info',
            name='coupon_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Coupons_Item', verbose_name='쿠폰이름'),
        ),
        migrations.AlterField(
            model_name='coupon_item_info',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info', verbose_name='소유자'),
        ),
        migrations.AlterField(
            model_name='coupons_item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Items', verbose_name='쿠폰이 적용된 상품'),
        ),
        migrations.AlterField(
            model_name='customer_info',
            name='sex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Sex_Info', verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='item_info',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Items', verbose_name='상품'),
        ),
        migrations.AlterField(
            model_name='items',
            name='sort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Item_Sort_Info', verbose_name='상품종류'),
        ),
        migrations.AlterField(
            model_name='mv_history',
            name='camera_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Camera_Info', verbose_name='카메라 번호'),
        ),
        migrations.AlterField(
            model_name='mv_history',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info', verbose_name='이동고객'),
        ),
        migrations.AlterField(
            model_name='pur_history',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info', verbose_name='구매고객'),
        ),
        migrations.AlterField(
            model_name='pur_history',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Items', verbose_name='구매상품'),
        ),
    ]
