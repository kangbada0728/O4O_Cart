package com.example.jewi9.myapplicationo4o;

import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.widget.ListView;

import org.json.JSONException;
import org.json.JSONObject;

public class Popular extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.popularlist);

        Menu menu = new Menu();
        ListView listview;
        ListViewAdapter adapter;

        //adapter생성
        adapter = new ListViewAdapter();

        // 리스트뷰 참조 및 Adapter달기
        listview = (ListView) findViewById(R.id.listview1);
        listview.setAdapter(adapter);

        for(int i = 0 ;i<menu.product_jsonobject.length()-1;i++){
            try {
                //product에 item1,2... 들을 각각 넣는다.
                JSONObject product = (JSONObject)menu.product_jsonobject.get("popular"+Integer.toString(i+1));
                String name = product.getString("name"); name = Integer.toString(i+1) + ". " + name;

                adapter.addItem(ContextCompat.getDrawable(this, R.drawable.ic_launcher_background), name, "");

            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }
}


