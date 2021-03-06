package com.example.jewi9.myapplicationo4o;

import android.content.Context;
import android.graphics.drawable.Drawable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.CheckBox;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

public class ListViewAdapter_Coupon extends BaseAdapter {

    // Adapter에 추가된 데이터를 저장하기 위한 ArrayList
    private ArrayList<ListViewItem_Coupon> listViewItemList = new ArrayList<ListViewItem_Coupon>() ;

    // ListViewAdapter의 생성자
    public ListViewAdapter_Coupon() {

    }

    @Override
    public int getCount() {
        return listViewItemList.size() ;
    }

    @Override
    public Object getItem(int position) {
        return listViewItemList.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        final int pos = position;
        final Context context = parent.getContext();
        //ViewHolder holder = null;


        // "listview_item" Layout을 inflate하여 convertView 참조 획득.
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.coupon_custom_list_view, parent, false);

            /*holder = new ViewHolder();
            holder.serial = (TextView) convertView.findViewById(R.id.textView4);
            holder.cbox = (CheckBox) convertView.findViewById(R.id.checkBox1);
            convertView.setTag(holder);
            holder.serial.setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View v) {
                    CheckBox cb = (CheckBox) v;

                }
            });*/
        }

        // 화면에 표시될 View(Layout이 inflate된)으로부터 위젯에 대한 참조 획득
        ImageView iconImageView = (ImageView) convertView.findViewById(R.id.imageView1) ;
        TextView CouponNameTextView = (TextView) convertView.findViewById(R.id.textView1) ;
        TextView DiscountRateTextView = (TextView) convertView.findViewById(R.id.textView2) ;
        TextView DueDateTextView = (TextView) convertView.findViewById(R.id.textView3);

        // Data Set(listViewItemList)에서 position에 위치한 데이터 참조 획득
        ListViewItem_Coupon listViewItem = listViewItemList.get(position);

        // 아이템 내 각 위젯에 데이터 반영
        iconImageView.setImageDrawable(listViewItem.getIcon());
        CouponNameTextView.setText(listViewItem.getCouponName());
        DiscountRateTextView.setText(listViewItem.getDiscount());
        DueDateTextView.setText(listViewItem.getdueDate());

        return convertView;
    }
    private class ViewHolder{
        TextView serial;
        CheckBox cbox;
    }
    // 아이템 데이터 추가를 위한 함수. 개발자가 원하는대로 작성 가능.
    public void addItem(Drawable icon, String couponName, String discountRate, String dueDate) {
        ListViewItem_Coupon item = new ListViewItem_Coupon();

        item.setIcon(icon);
        item.setCouponName(couponName);
        item.setDiscount(discountRate);
        item.setdueDate(dueDate);

        listViewItemList.add(item);
    }
}