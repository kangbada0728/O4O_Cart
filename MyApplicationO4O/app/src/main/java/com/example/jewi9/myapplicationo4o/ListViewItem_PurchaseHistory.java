package com.example.jewi9.myapplicationo4o;

import android.graphics.drawable.Drawable;

public class ListViewItem_PurchaseHistory {
    private Drawable iconDrawable;
    private String product;
    private String price;
    private String purchaseDate;

    public void setIcon(Drawable icon){
        iconDrawable=icon;
    }
    public void setProduct(String pro){
        product=pro;
    }
    public void setPrice(String pri){
        price=pri;
    }
    public void setTime(String t){
        purchaseDate=t;
    }

    public Drawable getIcon(){
        return this.iconDrawable;
    }
    public String getProduct(){
        return this.product;
    }
    public String getPrice(){
        return this.price;
    }
    public String getTime(){
        return this.purchaseDate;
    }
}
