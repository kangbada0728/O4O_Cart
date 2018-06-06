package com.example.jewi9.cashier;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

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

import static com.example.jewi9.cashier.MainActivity.jsonObject;

public class InputUserID extends AppCompatActivity
{

    private EditText id;
    public static String id_string;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.input_user_id);

        id = (EditText) findViewById(R.id.id);
        Log.d("productinInput@@@@@@", "productinInput@@@@@@: " + jsonObject);

        Button complete_barcode = (Button) findViewById(R.id.complete);
        complete_barcode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                id_string = id.getText().toString();

                class BtnAsyncTask extends AsyncTask {

                    String result="";
                    String url = "http://192.168.0.26:8000/cart/do_payment/";
                    @Override
                    protected Object doInBackground(Object[] objects) {
                        String json = "";
                        try {
                            jsonObject.accumulate("id", id_string);

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                        json = jsonObject.toString();
                        Log.d("productinInput@@@@@@", "productinInput@@@@@@: " + json);

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
                Intent i = new Intent( InputUserID.this, MainActivity.class);
                startActivity(i);
            }
        });
    }
}
