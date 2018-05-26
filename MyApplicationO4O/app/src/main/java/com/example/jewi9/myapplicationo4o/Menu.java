package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.protocol.HTTP;
import org.json.JSONException;
import org.json.JSONObject;

import com.google.firebase.iid.FirebaseInstanceId;

import java.io.IOException;
import java.io.UnsupportedEncodingException;

public class Menu extends AppCompatActivity
{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.menu);
    }


    public void onClickCompare(View view) {
        Intent intent = new Intent(Menu.this, Compare.class);
        startActivity(intent);
    }

    /*쿠폰보기 버튼 클릭*/
    public void onClickCoupon(View view)
    {
        //서버에 요청을 보낸다.(보낼값: token, id)
        class BtnAsyncTask extends AsyncTask {
            MainActivity mainactivity = new MainActivity();
            String result="";
            String url = "http://192.168.1.150:8000/requestCoupon";//나중에 원격서버주소로 변경!!!!!!!!!

            @Override
            protected Object doInBackground(Object[] objects) {
                String json="";
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject.accumulate("token",FirebaseInstanceId.getInstance().getToken());
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                try {
                    jsonObject.accumulate("id",mainactivity.id_string);
                    Log.d("id", "id@@@@@@ in Menu.java: " + mainactivity.id_string);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                json = jsonObject.toString();
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

            Intent intent = new Intent( Menu.this, Coupon.class);
            startActivity( intent );
    }
}