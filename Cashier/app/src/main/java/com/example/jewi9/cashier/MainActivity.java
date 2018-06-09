package com.example.jewi9.cashier;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Parcelable;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.FrameLayout;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.Toast;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

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
import java.io.Serializable;
import java.io.UnsupportedEncodingException;

public class MainActivity extends AppCompatActivity {
    String barcode=null;
     JSONObject  jsonObject = new JSONObject();

    int number_of_product = 0;
    //private ImageButton setting_btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    protected void onResume(){
        super.onResume();
        IntentIntegrator integrator = new IntentIntegrator(this);
        integrator.setCaptureActivity(BarcodeScan.class);
        integrator.initiateScan();
    }
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent intent)//바코드
    {
        if (resultCode == Activity.RESULT_OK) {
            IntentResult scanResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, intent);

            barcode = scanResult.getContents();
            Toast.makeText(this, barcode, Toast.LENGTH_LONG).show();

            try {
                jsonObject.accumulate("serial"+(number_of_product+1), barcode);
                number_of_product++;
                } catch (JSONException e) {
                 e.printStackTrace();
                }
        }
        if(resultCode == RESULT_CANCELED)
        {
            Intent i = new Intent( MainActivity.this, InputUserID.class);
            Log.d("@@@@@@PP","@@@@@@PP" + jsonObject.toString());

            i.putExtra("json", jsonObject.toString());

            startActivity(i);
        }
    }
}