package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import com.journeyapps.barcodescanner.CaptureActivity;

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

public class CartPairing extends AppCompatActivity
{
    /* QR code scanner 객체 */
    private IntentIntegrator qrScan;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        /* QR code Scanner Setting */
        qrScan = new IntentIntegrator(this);
        qrScan.setPrompt("카트 QR에 카메라를 대세요.");
        qrScan.setCaptureActivity(CaptureActivityAnyOrientation.class);
        qrScan.setOrientationLocked(false);
        qrScan.initiateScan();
    }

    /* Getting the Scan Results */
    @Override
    protected void onActivityResult(int requestCode,int resultCode,Intent data)
    {
        IntentResult result = IntentIntegrator.parseActivityResult(requestCode, resultCode, data);
        if (result != null) {
            if (result.getContents() == null) {
                Log.v("qrcode@@@@@@", "no contents");
            } else {
                /* QR 코드 내용*/
                final String cartID = result.getContents();
                Log.v("qrcode Contents@@@@@@", cartID);

                class BtnAsyncTask extends AsyncTask
                {
                    String result="";
                    String url = "http://"+MainActivity.ipAddress+"/cart/cart_paring/";
                    @Override
                    protected Object doInBackground(Object[] objects)
                    {
                        String json="";
                        JSONObject jsonObject = new JSONObject();
                        try {
                            jsonObject.accumulate("serial",cartID);
                            jsonObject.accumulate("id",MainActivity.id_string);
                            Log.d("cartpair@@@@@@","cartpair@@@@@@"+jsonObject);
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
                Intent intent = new Intent(getApplicationContext(), Menu.class);
                startActivity(intent);
            }
        }
        else{
            super.onActivityResult(requestCode,resultCode,data);
        }
    }
}
