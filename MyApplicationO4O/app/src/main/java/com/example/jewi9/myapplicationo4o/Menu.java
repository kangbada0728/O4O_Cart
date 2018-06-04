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

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

import java.io.IOException;
import java.io.UnsupportedEncodingException;

public class Menu extends AppCompatActivity
{
    /*메뉴를 만들기위한 변수들*/
    private ListView menuList;
    private FrameLayout menuContainer;
    private DrawerLayout menuDrawer;
    private final String[] menuItems = {"카트 페어링","가격 비교", "보유 쿠폰","구매 내역"};

    public static JSONObject coupon_jsonobject;
    public static JSONObject product_jsonobject;
    public static JSONObject pur_history_jsonobj;
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
                String result="";
                String url = "http://192.168.28.219:8000/cart/comparing_product/";//나중에 원격서버주소로 변경!!!!!!!!!
                @Override
                protected void onPostExecute(Object o) {
                    super.onPostExecute(o);
                    Intent intent = new Intent( Menu.this, Swipe_Compare.class);
                    startActivity(intent);

                }
                @Override
                protected Object doInBackground(Object[] objects) {
                    String json="";
                    JSONObject jsonObject = new JSONObject();

                    try {
                        jsonObject.accumulate("serial",barcode);
                        Log.d("barcodeSerial", "barcodeSerial@@@@@@ in Menu.java: " + barcode);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    json = jsonObject.toString();
                    try {
                        result = goHttpPost(url, json);
                        Log.d("productresult@@@@@@", "productResult@@@@@@: " + result);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                    try {
                        product_jsonobject = new JSONObject(result);
                    } catch (JSONException e) {
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
    }



    /*쿠폰보기 버튼 클릭*/
    public void onClickCoupon(View view)
    {
        //서버에 요청을 보낸다.(보낼값: token, id)
        class BtnAsyncTask extends AsyncTask {
            String result="";
            String url = "http://192.168.28.219:8000/cart/coupon_check/";

            @Override
            protected void onPostExecute(Object o) {
                super.onPostExecute(o);
                Intent intent = new Intent( Menu.this, Coupon.class);
                startActivity( intent );
            }

            @Override
            protected Object doInBackground(Object[] objects) {
                String json="";
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject.accumulate("token",FirebaseInstanceId.getInstance().getToken());
                    Log.d("token", "token@@@@@@ in Menu.java: " + FirebaseInstanceId.getInstance().getToken());
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
                Log.d("result@@@@@@", "result1@@@@@@: " + result);
                try {
                    coupon_jsonobject = new JSONObject(result);
                } catch (JSONException e) {
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
    public void onClickPairing(View view)
    {
        IntentIntegrator integrator = new IntentIntegrator(this);
        integrator.setCaptureActivity(CartPairing.class);
        integrator.initiateScan();
    }

    public void onClickPurHistory(View view)
    {
        //서버에 요청을 보낸다.(보낼값: token, id)
        class BtnAsyncTask extends AsyncTask {
            String result="";
            String url = "http://192.168.28.219:8000/cart/pur_history/";

            @Override
            protected void onPostExecute(Object o) {
                super.onPostExecute(o);
                Intent intent = new Intent( Menu.this, PurchaseHistory.class);
                startActivity( intent );
            }

            @Override
            protected Object doInBackground(Object[] objects) {
                String json="";
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject.accumulate("id",MainActivity.id_string);
                    //나중에 시간정보도 함께 넘겨야 됨.!!!!!!
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                json = jsonObject.toString();
                try {
                    result = goHttpPost(url, json);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                Log.d("resultPur@@@@@@", "resultPur@@@@@@: " + result);
                try {
                    pur_history_jsonobj = new JSONObject(result);
                } catch (JSONException e) {
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