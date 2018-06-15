package com.example.jewi9.myapplicationo4o;

import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.widget.ListView;

import org.json.JSONException;
import org.json.JSONObject;

public class ProductInfo extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.productinfo);

        Menu menu = new Menu();
        ListView listview;
        ListViewAdapter adapter;

        //adapter생성
        adapter = new ListViewAdapter();

        // 리스트뷰 참조 및 Adapter달기
        listview = (ListView) findViewById(R.id.listview1);
        listview.setAdapter(adapter);

        try {
            JSONObject product = (JSONObject)menu.product_jsonobject.get("item_info");
            String name = product.getString("item_name");
            String expireDate = product.getString("expire_date"); expireDate = "유통기한" + expireDate;
            String price = product.getString("price"); price = price +"원";

            adapter.addItem(ContextCompat.getDrawable(this, R.drawable.o4o), name, price, expireDate);
        } catch (JSONException e) {
            e.printStackTrace();
        }

    }
}
