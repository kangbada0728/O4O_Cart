package com.example.jewi9.myapplicationo4o;

import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.ListView;

import org.json.JSONException;
import org.json.JSONObject;

public class PurchaseHistory extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.purchasehistorylist);

        Purchase_History_Select_Date purchase_history_select_date = new Purchase_History_Select_Date();
        ListView listview;
        ListViewAdapter adapter;


        //adapter생성
        adapter = new ListViewAdapter();

        // 리스트뷰 참조 및 Adapter달기
        listview = (ListView) findViewById(R.id.listview1);
        listview.setAdapter(adapter);

        for(int i = 0 ;i<purchase_history_select_date.pur_history_jsonobj.length()-1;i++)
        {
            try {
                JSONObject productHistory= (JSONObject)purchase_history_select_date.pur_history_jsonobj.get("history"+Integer.toString(i+1));
                Log.d("@@@@@@purchase","@@@@@@purchase"+productHistory);
                String productName = productHistory.getString("item");
                String price = productHistory.getString("price"); price = price + "원";
                String purchaseDate = productHistory.getString("time");

                adapter.addItem(ContextCompat.getDrawable(this, R.drawable.o4o), productName, price,purchaseDate);
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }
}
