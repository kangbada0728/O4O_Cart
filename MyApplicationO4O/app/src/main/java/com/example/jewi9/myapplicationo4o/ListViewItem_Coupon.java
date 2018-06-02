package com.example.jewi9.myapplicationo4o;

import android.graphics.drawable.Drawable;

public class ListViewItem_Coupon {
    private Drawable icon ;
    private String discount ;
    private String couponName;

    public void setIcon(Drawable icon) {
        this.icon = icon ;
    }
    public void setCouponName(String couponName) {
        this.couponName = couponName ;
    }
    public void setDiscount(String discount) {
        this.discount = discount ;
    }

    public Drawable getIcon() {
        return this.icon ;
    }
    public String getCouponName() {
        return this.couponName ;
    }
    public String getDiscount() {
        return this.discount ;
    }
}