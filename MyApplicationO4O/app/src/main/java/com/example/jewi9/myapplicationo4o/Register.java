package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;

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



public class Register extends AppCompatActivity
{
    private EditText id;
    private EditText pw;
    private EditText age;
    private RadioButton male;
    private RadioButton female;

    private String id_string, pw_string;
    private int age_Int;
    private String sex_string;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.register);

        id = (EditText)findViewById( R.id.ID );
        pw = (EditText)findViewById( R.id.PW );
        age = (EditText)findViewById( R.id.age );
        male = (RadioButton)findViewById( R.id.male );
        female = (RadioButton)findViewById( R.id.female );

        View.OnClickListener listener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if( male.isChecked() ) {
                    sex_string = "M";
                }
                else if( female.isChecked()) {
                    sex_string = "F";
                }
                id_string = id.getText().toString();
                pw_string = pw.getText().toString();
                age_Int = Integer.parseInt(age.getText().toString());

                class BtnAsyncTask extends AsyncTask {
                    String result = "";
                    String url = "http://192.168.19.36:8000/regist";//나중에 원격서버주소로 변경!!!!!!!!!

                    @Override
                    protected Object doInBackground(Object[] objects) {
                        String json = "";
                        JSONObject jsonObject = new JSONObject();
                        try {
                            jsonObject.accumulate("id",id_string);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                        try {
                            jsonObject.accumulate("pw",pw_string);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                        try {
                            jsonObject.accumulate("age",age_Int);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                        try {
                            jsonObject.accumulate("sex",sex_string);
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
                Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(intent);
            }
        };
        Button btn_reg_complete = (Button) findViewById(R.id.button);
        btn_reg_complete.setOnClickListener(listener);
    }
}