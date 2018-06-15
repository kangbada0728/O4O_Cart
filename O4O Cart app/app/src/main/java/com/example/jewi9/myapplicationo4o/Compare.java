package com.example.jewi9.myapplicationo4o;

import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;

import android.util.Log;
import android.widget.ListView;

import org.json.JSONException;
import org.json.JSONObject;

public class Compare extends AppCompatActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.comparelist);

        Menu menu = new Menu();
        ListView listview;
        ListViewAdapter adapter;


        //adapter생성
        adapter = new ListViewAdapter();

        // 리스트뷰 참조 및 Adapter달기
        listview = (ListView) findViewById(R.id.listview1);
        listview.setAdapter(adapter);

        Log.d("prodcutjson@@@@@@", "prodcutjson@@@@@@ " + menu.product_jsonobject);

        for(int i = 0 ;i<menu.product_jsonobject.length()-1;i++){
            try {
                //product에 item1,2... 들을 각각 넣는다.
                JSONObject  product = (JSONObject)menu.product_jsonobject.get("item"+Integer.toString(i+1));
                String name = product.getString("name");
                String price = product.getString("price"); price = price + "원";

                adapter.addItem(ContextCompat.getDrawable(this, R.drawable.o4o), name, price,"");

            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }

}
