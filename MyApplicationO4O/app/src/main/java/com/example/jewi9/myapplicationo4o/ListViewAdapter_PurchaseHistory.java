package com.example.jewi9.myapplicationo4o;

import android.content.Context;
import android.graphics.drawable.Drawable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

public class ListViewAdapter_PurchaseHistory extends BaseAdapter {

    private ArrayList<ListViewItem_PurchaseHistory> listViewItemList = new ArrayList<ListViewItem_PurchaseHistory>() ;

    // ListViewAdapter의 생성자
    public ListViewAdapter_PurchaseHistory() {

    }

    @Override
    public int getCount() {
        return listViewItemList.size() ;
    }

    @Override
    public Object getItem(int position) {
        return listViewItemList.get(position) ;
    }

    @Override
    public long getItemId(int position) {
        return position ;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        final int pos = position;
        final Context context = parent.getContext();

        // "listview_item" Layout을 inflate하여 convertView 참조 획득.
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.purchasehistory_custom_list_view, parent, false);
        }

        ImageView iconImageView = (ImageView) convertView.findViewById(R.id.imageView1) ;
        TextView productNameTextView = (TextView) convertView.findViewById(R.id.textView1) ;
        TextView productPrice = (TextView) convertView.findViewById(R.id.textView2) ;
        TextView purchaseDate = (TextView) convertView.findViewById(R.id.textView3);
        // Data Set(listViewItemList)에서 position에 위치한 데이터 참조 획득
        ListViewItem_PurchaseHistory listViewItem = listViewItemList.get(position);

        // 아이템 내 각 위젯에 데이터 반영
        iconImageView.setImageDrawable(listViewItem.getIcon());
        productNameTextView.setText(listViewItem.getProduct());
        productPrice.setText(listViewItem.getPrice());
        purchaseDate.setText(listViewItem.getTime());
        return convertView;
    }
    public void addItem(Drawable icon, String productName, String price   , String purchaseDate) {
        ListViewItem_PurchaseHistory item = new ListViewItem_PurchaseHistory();

        item.setIcon(icon);
        item.setProduct(productName);
        item.setPrice(price);
        item.setTime(purchaseDate);
        listViewItemList.add(item);
    }
}
