package com.example.jewi9.myapplicationo4o;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.DatePicker;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.protocol.HTTP;
import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Purchase_History_Select_Date extends Activity {
    DatePicker StartDate;
    TextView StartTxtDate;
    DatePicker EndDate;
    TextView EndTxtDate;

    long StartTimestamp;
    long EndTimestamp;
    public static JSONObject pur_history_jsonobj;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.purchasehistory_selectdate);

        StartDate = (DatePicker) findViewById(R.id.datepicker1);
        StartTxtDate = (TextView) findViewById(R.id.txtdate1);
        EndDate = (DatePicker)findViewById(R.id.datepicker2);
        EndTxtDate = (TextView) findViewById(R.id.txtdate2);


        StartDate.init(StartDate.getYear(), StartDate.getMonth(), StartDate.getDayOfMonth(),
                new DatePicker.OnDateChangedListener() {

                    @Override
                    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                        StartTxtDate.setText(String.format("%d/%d/%d", year, monthOfYear + 1, dayOfMonth));
                    }
                });
        EndDate.init(EndDate.getYear(), EndDate.getMonth(), EndDate.getDayOfMonth(),
                new DatePicker.OnDateChangedListener() {

                    @Override
                    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                        EndTxtDate.setText(String.format("%d/%d/%d", year, monthOfYear + 1, dayOfMonth));
                    }
                });


        /*구매내역확인 버튼을 눌렀을때*/
        findViewById(R.id.show_purchase_history).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                String StartDateResult = String.format("%d-%d-%d", StartDate.getYear(), StartDate.getMonth() + 1, StartDate.getDayOfMonth());
                String EndDateResult = String.format("%d-%d-%d", EndDate.getYear(),EndDate.getMonth()+1, EndDate.getDayOfMonth());

                SimpleDateFormat changeTimestamp = new SimpleDateFormat("yyyy-MM-dd");
                try {
                    Date startdate = changeTimestamp.parse(StartDateResult);
                    Date enddate = changeTimestamp.parse(EndDateResult);
                     StartTimestamp = startdate.getTime();
                     EndTimestamp = enddate.getTime();
                    Log.i("sstimestamp@@@@@@@","sstimestamp@@@@@@"+String.valueOf(StartTimestamp));
                    Log.i("eetimestamp@@@@@@@","eetimestamp@@@@@@"+String.valueOf(EndTimestamp));
                } catch (ParseException e) {
                    e.printStackTrace();
                }
                class BtnAsyncTask extends AsyncTask {
                    String result="";
                    String url = "http://192.168.0.2:8000/cart/pur_history/";

                    @Override
                    protected void onPostExecute(Object o) {
                        super.onPostExecute(o);
                        Intent intent = new Intent( Purchase_History_Select_Date.this, PurchaseHistory.class);
                        startActivity( intent );
                    }

                    @Override
                    protected Object doInBackground(Object[] objects) {
                        String json="";
                        JSONObject jsonObject = new JSONObject();
                        try {
                            jsonObject.accumulate("id",MainActivity.id_string);
                            jsonObject.accumulate("start_date",StartTimestamp);
                            jsonObject.accumulate("end_date",EndTimestamp);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                        json = jsonObject.toString();
                        Log.d("resultPur@@@@@@", "resultPur@@@@@@: " + json);

                        try {
                            result = goHttpPost(url, json);
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
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
        });
        /*class BtnAsyncTask extends AsyncTask {
            String result="";
            String url = "http://192.168.0.2:8000/cart/pur_history/";

            @Override
            protected void onPostExecute(Object o) {
                super.onPostExecute(o);
                Intent intent = new Intent( Purchase_History_Select_Date.this, PurchaseHistory.class);
                startActivity( intent );
            }

            @Override
            protected Object doInBackground(Object[] objects) {
                String json="";
                JSONObject jsonObject = new JSONObject();
                try {
                    jsonObject.accumulate("id",MainActivity.id_string);
                    jsonObject.accumulate("start_date",StartTimestamp);
                    jsonObject.accumulate("end_date",EndTimestamp);
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                json = jsonObject.toString();
                Log.d("resultPur@@@@@@", "resultPur@@@@@@: " + json);

                try {
                    result = goHttpPost(url, json);
                } catch (IOException e) {
                    e.printStackTrace();
                }
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
        async.execute();*/
    }
}
