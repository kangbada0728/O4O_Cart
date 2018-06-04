package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.util.SparseArray;
import android.util.SparseBooleanArray;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.protocol.HTTP;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashMap;

public class Coupon extends AppCompatActivity {
   // private ArrayList<HashMap<String,String>> Data = new ArrayList<HashMap<String, String>>();
    Menu menu = new Menu();
    private ListView listView;
    int num_of_coupon;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.couponlist);

        ListViewAdapter_Coupon adapter;
        listView =(ListView)findViewById(R.id.List_view);
        adapter = new ListViewAdapter_Coupon() ;

        num_of_coupon = menu.coupon_jsonobject.length();

        // 리스트뷰 참조 및 Adapter달기
        listView.setAdapter(adapter);

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
        //쿠폰 적용버튼을 클릭함
        applyCoupon.setOnClickListener(new Button.OnClickListener()
        {
            SparseBooleanArray checkedItems = listView.getCheckedItemPositions();
            JSONObject selectedCoupon = new JSONObject();
            JSONObject serial = new JSONObject();

            @Override
            public void onClick(View v)
            {
                class BtnAsyncTask extends AsyncTask
                {
                    String result="";
                    String url = "http://192.168.28.219:8000/cart/change_coupon_state/";
                    //int num_of_selected=0;

                    @Override
                    protected Object doInBackground(Object[] objects) {
                        String json="";
                        int j = 0;
                        for(int i=0 ;i<num_of_coupon;i++){
                            if(checkedItems.get(i)){
                                try {
                                    selectedCoupon = (JSONObject)menu.coupon_jsonobject.get("coupon"+Integer.toString(i+1));
                                    serial.accumulate("serial"+(j+1),selectedCoupon.getString("serial_num"));
                                    j++;
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                            }
                        }

                        Log.d("selectedSerial@@@@@@","selectedSerial@@@@@@"+serial);
                        json = serial.toString();
                        try {
                            result = goHttpPost(url, json);
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        return null;
                    }
                    public String goHttpPost(String host, String json) throws ClientProtocolException, IOException {
                        String msg = null; //http 연결 인증
                        DefaultHttpClient client = new DefaultHttpClient();
                        HttpPost httppost = new HttpPost(host);

                        try {
                            httppost.setEntity(new StringEntity(json, HTTP.UTF_8));
                        }
                        catch (UnsupportedEncodingException e) { // TODO Auto-generated catch block e.printStackTrace();
                        }
                        ResponseHandler responseHandler = new BasicResponseHandler();
                        msg = (String) client.execute(httppost, responseHandler);

                        return msg;
                    }
                }
                BtnAsyncTask async = new BtnAsyncTask();
                async.execute();
            }
        });
    }
}