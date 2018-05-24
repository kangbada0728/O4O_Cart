package com.example.jewi9.myapplicationo4o;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class Coupon extends AppCompatActivity {
    private ArrayList<String> values = new ArrayList<String>();
    private ArrayAdapter<String> adapter;
    private String id;

    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.coupon);

        ListView couponList = (ListView) findViewById( R.id.couponList);

        adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, values);
        couponList.setAdapter( adapter );
        couponList.setOnItemClickListener( new AdapterView.OnItemClickListener(){
            public void onItemClick(AdapterView<?> parent, View view, int position, long id)
            {
                String item = values.get( position );
                int no = Integer.parseInt(""+ item.charAt( item.length() -1 ) );

                if( no > 1)
                {
                    String refinedStr = item.substring( 0, item.length() - 1  );
                    no--;
                    item = refinedStr + no;

                    values.remove(position);
                    values.add( position, item);
                    adapter.notifyDataSetChanged();
                    //서버에 개수 줄이기 요구
                }
                else
                {
                    values.remove(position);
                    adapter.notifyDataSetChanged();
                    Toast.makeText(Coupon.this, item + " removed", Toast.LENGTH_LONG).show();
                    //서버에 쿠폰 제거 요구
                }
            }
        });
    }
}
