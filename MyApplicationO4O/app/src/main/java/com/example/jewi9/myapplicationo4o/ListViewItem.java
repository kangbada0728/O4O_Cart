package com.example.jewi9.myapplicationo4o;
import android.graphics.drawable.Drawable;


public class ListViewItem {
    private Drawable iconDrawable ;
    private String titleStr ;
    private String descStr ;
    private String expireDate ;

    public void setIcon(Drawable icon) {
        iconDrawable = icon ;
    }
    public void setTitle(String title) {
        titleStr = title ;
    }
    public void setDesc(String desc) {
        descStr = desc ;
    }
    public void setExpire(String expire){
        expireDate = expire;
    }

    public Drawable getIcon() {
        return this.iconDrawable ;
    }
    public String getTitle() {
        return this.titleStr ;
    }
    public String getDesc() {
        return this.descStr ;
    }
    public String getExpire(){return this.expireDate;}
}
