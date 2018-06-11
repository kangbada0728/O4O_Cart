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
import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
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
                    @Override
                    protected void onPostExecute(Object o) {
                        super.onPostExecute(o);
                        Intent intent = new Intent( Purchase_History_Select_Date.this, PurchaseHistory.class);
                        startActivity( intent );
                    }

                    @Override
                    protected Object doInBackground(Object[] objects) {
                        InputStream inputStream = null;
                        String result="";
                        try {
                            HttpClient client = new DefaultHttpClient();
                            String getURL = "http://"+MainActivity.ipAddress+"/cart/pur_history/" + MainActivity.id_string + "/" + StartTimestamp +"/"+ EndTimestamp+"/";

                            HttpGet get = new HttpGet(getURL);
                            HttpResponse responseGet = client.execute(get);
                            inputStream = responseGet.getEntity().getContent();
                            if (inputStream != null) {
                                result = convertInputStreamToString(inputStream);
                                pur_history_jsonobj = new JSONObject(result);
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
        });

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
}
