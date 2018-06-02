package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;

public class Coupon extends AppCompatActivity {
   // private ArrayList<HashMap<String,String>> Data = new ArrayList<HashMap<String, String>>();
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.couponlist);

        ListViewAdapter_Coupon adapter;
        listView =(ListView)findViewById(R.id.List_view);
        adapter = new ListViewAdapter_Coupon() ;

        // 리스트뷰 참조 및 Adapter달기
        listView.setAdapter(adapter);

        Menu menu = new Menu();
        Log.d("Coupon@@@@@@", "CouponARray in Coupon @@@@@@: " + menu.coupon_jsonobject);

        for(int i=0;i<menu.coupon_jsonobject.length();i++){
            try {
                JSONObject coupon = (JSONObject)menu.coupon_jsonobject.get("coupon"+Integer.toString(i+1));
                String name = coupon.getString("name");
                String discountRate = coupon.getString("discount"); discountRate = "할인율: " + discountRate + "%";
                String dueDate = coupon.getString("datetime");  dueDate = "사용기한: " + dueDate;
                adapter.addItem(ContextCompat.getDrawable(this,R.drawable.ic_launcher_background),name,discountRate,dueDate);
            } catch (JSONException e) {
                e.printStackTrace();
            }

        }
        Button applyCoupon = (Button)findViewById(R.id.apply);
        applyCoupon.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });
    }
}