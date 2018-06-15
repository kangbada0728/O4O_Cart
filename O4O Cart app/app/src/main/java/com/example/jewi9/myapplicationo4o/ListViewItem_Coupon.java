package com.example.jewi9.myapplicationo4o;

import android.graphics.drawable.Drawable;

public class ListViewItem_Coupon {
    private Drawable icon ;
    private String discount ;
    private String couponName;
    private String dueDate;
    private String serial;
    //private String cbox = null;
    //boolean selected = false;

    /*public ListViewItem_Coupon(String serial,String cbox,boolean selected){
        super();
        this.serial = serial;
        this.cbox = cbox;
        this.selected = selected;
    }
    public void setSelected(boolean selected){
        this.selected=selected;
    }
    public  boolean isSelected(){
        return selected;
    }
    public void setCbox(String cbox){
        this.cbox =cbox;
    }
    public String getCbox(){
        return cbox;
    }

*/

    public void setIcon(Drawable icon) {
        this.icon = icon ;
    }
    public void setCouponName(String couponName) {
        this.couponName = couponName ;
    }
    public void setDiscount(String discount) {
        this.discount = discount ;
    }
    public void setdueDate(String dueDate){
        this.dueDate = dueDate;
    }
    public void setSerial(String serial){
        this.serial = serial;
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
    public String getdueDate(){
        return this.dueDate;
    }
    public String getSerial(){
        return this.serial;
    }

}