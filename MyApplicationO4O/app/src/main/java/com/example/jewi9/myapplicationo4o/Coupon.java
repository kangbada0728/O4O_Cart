package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;

public class Coupon extends AppCompatActivity {
    private ArrayList<HashMap<String,String>> Data = new ArrayList<HashMap<String, String>>();
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.couponlist);

        listView =(ListView)findViewById(R.id.List_view);

        Menu myMenu = new Menu();
        Log.d("Coupon@@@@@@", "CouponARray in Coupon @@@@@@: " + myMenu.coupon_jsonobject);

        //Menu.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        for(int i=0;i<myMenu.coupon_jsonobject.length();i++){
            try {
                HashMap<String,String> InputData1 = new HashMap<>();
                // Log.d("Coupon@@@@@@", "coupon"+Integer.toString(i+1));
                JSONObject coupon = (JSONObject)myMenu.coupon_jsonobject.get("coupon"+Integer.toString(i+1));
                //Log.d("Coupon@@@@@@", "object"+coupon);

                InputData1.put("name", coupon.getString("name"));
                //InputData1.put("discount",coupon.getString("discount"));
                InputData1.put("datetime",coupon.getString("datetime"));
                Data.add(InputData1);

            } catch (JSONException e) {
                e.printStackTrace();
            }

        }
        /*adapter생성*/
        SimpleAdapter simpleAdapter = new SimpleAdapter(this,Data,android.R.layout.simple_list_item_2,new String[]{"name","datetime"},new int[]{android.R.id.text1,android.R.id.text2});
        listView.setAdapter(simpleAdapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Intent intent = new Intent(getApplicationContext(),ClickCoupon.class);
                startActivity(intent);
            }
        });
    }
}