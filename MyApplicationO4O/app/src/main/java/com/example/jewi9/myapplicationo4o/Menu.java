package com.example.jewi9.myapplicationo4o;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ListView;
import android.widget.Toast;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.protocol.HTTP;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.Map;

public class Menu extends AppCompatActivity
{
    /*메뉴를 만들기위한 변수들*/
    private ListView menuList;
    private FrameLayout menuContainer;
    private DrawerLayout menuDrawer;
    private final String[] menuItems = {"카트 페어링","가격 비교", "보유 쿠폰","구매 내역"};

    public static JSONObject coupon_jsonobject;
    public static JSONObject product_jsonobject;
    String barcode=null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.menu);


        menuList = (ListView)findViewById(R.id.lv_activity_main_nav_list);
        menuContainer = (FrameLayout)findViewById(R.id.fl_activity_main_container);

        menuDrawer = (DrawerLayout)findViewById(R.id.dl_activity_main_drawer);
        menuList.setAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, menuItems));
        menuList.setOnItemClickListener(new DrawerItemClickListener());
    }

    public void onClickCompare(View view) {
        IntentIntegrator integrator = new IntentIntegrator(this);
        integrator.setCaptureActivity(BarcodeScan.class);
        integrator.initiateScan();
    }
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent intent)//바코드
    {
        if (resultCode == Activity.RESULT_OK)
        {
            IntentResult scanResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, intent);

            barcode = scanResult.getContents();
            Toast.makeText(this, barcode, Toast.LENGTH_LONG).show();

            class BtnAsyncTask extends AsyncTask {

                @Override
                protected void onPostExecute(Object o) {
                    super.onPostExecute(o);
                    Intent intent = new Intent( Menu.this, Swipe_Compare.class);
                    startActivity(intent);
                }
                @Override
                protected Object doInBackground(Object[] objects) {
                    InputStream inputStream = null;
                    String result="";
                    try {
                        HttpClient client = new DefaultHttpClient();
                        String getURL = "http://192.168.19.22:8000/cart/comparing_product/" + barcode + "/";

                        HttpGet get = new HttpGet(getURL);
                        HttpResponse responseGet = client.execute(get);
                        inputStream = responseGet.getEntity().getContent();
                        if (inputStream != null) {
                            result = convertInputStreamToString(inputStream);
                            product_jsonobject = new JSONObject(result);
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    return null;
                }
            }
            BtnAsyncTask async = new BtnAsyncTask();
            async.execute();
        }
    }

    /*쿠폰보기 버튼 클릭*/
    public void onClickCoupon(View view)
    {
        class BtnAsyncTask extends AsyncTask {

            @Override
            protected void onPostExecute(Object o) {
                super.onPostExecute(o);
                Intent intent = new Intent( Menu.this, Coupon.class);
                startActivity(intent);
            }
            @Override
            protected Object doInBackground(Object[] objects) {
                InputStream inputStream = null;
                String result="";
                try {
                    HttpClient client = new DefaultHttpClient();
                    String getURL = "http://192.168.19.22:8000/cart/coupon_check/" + MainActivity.id_string + "/";

                    HttpGet get = new HttpGet(getURL);
                    HttpResponse responseGet = client.execute(get);
                    inputStream = responseGet.getEntity().getContent();
                    if (inputStream != null) {
                        result = convertInputStreamToString(inputStream);
                        coupon_jsonobject = new JSONObject(result);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                return null;
            }
        }
        BtnAsyncTask async = new BtnAsyncTask();
        async.execute();
    }
    public void onClickPairing(View view)
    {
        IntentIntegrator integrator = new IntentIntegrator(this);
        integrator.setCaptureActivity(CartPairing.class);
        integrator.initiateScan();
    }

    public void onClickPurHistory(View view)
    {
        Intent intent = new Intent( Menu.this, Purchase_History_Select_Date.class);
        startActivity( intent );
    }
    private static String convertInputStreamToString(InputStream inputStream) throws IOException{
        BufferedReader bufferedReader = new BufferedReader( new InputStreamReader(inputStream));
        String line = "";
        String result = "";
        while((line = bufferedReader.readLine()) != null)
            result += line;

        inputStream.close();
        return result;

    }
    private class DrawerItemClickListener implements android.widget.AdapterView.OnItemClickListener {

        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            switch (position) {
                case 0://페어링하기
                    onClickPairing(view);
                    break;
                case 1://가격비교
                    onClickCompare(view);
                    break;
                case 2://보유쿠폰확인
                    onClickCoupon(view);
                    break;
                case 3://구매내역
                    onClickPurHistory(view);
                    break;

            }
            menuDrawer.closeDrawer(menuList);
        }
    }
}
