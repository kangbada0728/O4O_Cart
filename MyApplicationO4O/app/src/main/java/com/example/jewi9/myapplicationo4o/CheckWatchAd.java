package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
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

import java.io.IOException;
import java.io.UnsupportedEncodingException;


public class CheckWatchAd extends AppCompatActivity {
    MyFirebaseMessagingService pushData = new MyFirebaseMessagingService();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.check_watch_ad);
    }

    /*광고 보기를 취소했을 때*/
    public void onClickCancelCheckAD(View view) {
        Intent intent = new Intent(CheckWatchAd.this, Menu.class);
        startActivity(intent);
    }

    /*광고보기를 클릭했을 때*/
    public void onClickCheckAD(View view) {
        class BtnAsyncTask extends AsyncTask {
            String result = "";
            String url = "http://192.168.28.219:8000/cart/send_coupon/";

            @Override
            protected Object doInBackground(Object[] objects) {
                String json = "";
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject.accumulate("item", pushData.pushData.getString("item"));
                    jsonObject.accumulate("id", MainActivity.id_string);
                    Log.d("cartpair@@@@@@", "cartpair@@@@@@" + jsonObject);
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
                } catch (UnsupportedEncodingException e) { // TODO Auto-generated catch block e.printStackTrace();
                }
                ResponseHandler responseHandler = new BasicResponseHandler();
                msg = (String) client.execute(httppost, responseHandler);

                return msg;
            }
        }
        BtnAsyncTask async = new BtnAsyncTask();
        async.execute();
        Intent intent = new Intent( CheckWatchAd.this, ShowAdPicture.class);
        startActivity( intent );
    }



}
