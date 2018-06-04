package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;

import com.google.firebase.iid.FirebaseInstanceId;

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

/*푸시 알림이 왔을 경우 보이는 창*/
public class Push extends AppCompatActivity
{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.push);
    }
    public void onClickWatchCoupon(View view)//쿠폰보기를 눌렀을 경우 쿠폰목록으로 이동한다.
    {
        //서버에 요청을 보낸다.(보낼값: token, id)
        class BtnAsyncTask extends AsyncTask {
            String result="";
            String url = "http://192.168.28.219:8000/requestCoupon";//나중에 원격서버주소로 변경!!!!!!!!!

            @Override
            protected Object doInBackground(Object[] objects) {
                String json="";
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject.accumulate("token", FirebaseInstanceId.getInstance().getToken());
                    Log.d("token", "token@@@@@@ in Menu.java: " + FirebaseInstanceId.getInstance().getToken());
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                try {
                    jsonObject.accumulate("id",MainActivity.id_string);
                    Log.d("id", "id@@@@@@ in Menu.java: " + MainActivity.id_string);
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
        Intent intent = new Intent( Push.this, Coupon.class);
        startActivity( intent );
    }
    public void onClickCancel(View view) //쿠폰보기를 취소했을 경우 Menu로 돌아간다.
    {
        Intent intent = new Intent( Push.this, Menu.class);
        startActivity( intent );
    }
}