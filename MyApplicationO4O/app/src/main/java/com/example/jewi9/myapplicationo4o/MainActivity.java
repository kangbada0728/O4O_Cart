package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.messaging.FirebaseMessaging;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.protocol.HTTP;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.UnsupportedEncodingException;

public class MainActivity extends AppCompatActivity {
    public static String ipAddress="192.168.23.169:8000";

    private EditText id;
    private EditText pw;

    public static String id_string;
    private String pw_string;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FirebaseMessaging.getInstance().subscribeToTopic("notice");
        FirebaseInstanceId.getInstance().getToken();

        id = (EditText) findViewById( R.id.id );
        pw = (EditText) findViewById( R.id.PW );

        Button btn_login = (Button) findViewById(R.id.login);
        btn_login.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                id_string = id.getText().toString();
                pw_string = pw.getText().toString();

                class BtnAsyncTask extends AsyncTask{

                    @Override
                    protected void onPostExecute(Object o) {
                        super.onPostExecute(o);
                        if(result.equals("200")){
                            Intent intent = new Intent(MainActivity.this,Menu.class);
                            startActivity(intent);//메뉴로 화면 전환!!
                        }
                    }
                    String result="";
                    String url = "http://"+MainActivity.ipAddress+"/cart/user_signin/";

                    @Override
                    protected Object doInBackground(Object[] objects) {
                        String json = "";
                        JSONObject jsonObject = new JSONObject();

                        try {
                            jsonObject.accumulate("id",id_string);
                            jsonObject.accumulate("pwd",pw_string);
                            jsonObject.accumulate("reg_id",FirebaseInstanceId.getInstance().getToken());

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }


                        json = jsonObject.toString();
                        try {
                            result = goHttpPost(url, json);
                            Log.d("@@@@@@login","@@@@@@login  "+result);

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

            }
        });
    }



    public void onClickRegister(View view )//회원가입 버튼 눌렀을때
    {
        Intent intent = new Intent( MainActivity.this, Register.class);
        startActivity( intent );
    }
}
