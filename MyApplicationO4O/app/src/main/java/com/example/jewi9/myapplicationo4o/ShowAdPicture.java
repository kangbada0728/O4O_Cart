    package com.example.jewi9.myapplicationo4o;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.util.Log;
import android.widget.ImageView;
import android.widget.LinearLayout;

import org.json.JSONException;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;

public class ShowAdPicture extends Activity {
    MyFirebaseMessagingService pushData = new MyFirebaseMessagingService();

    ImageView imageView01;
    Bitmap bitmap;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.show_ad_picture);

        imageView01 = (ImageView) findViewById(R.id.imageView01);
        String data_url = null;
        try {
            data_url = pushData.pushData.getString("link");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        final String finalData_url = data_url;
        Thread t = new Thread()
        {
            @Override
            public void run()
            {
                try{
                    URL url = new URL(finalData_url);
                    HttpURLConnection conn = (HttpURLConnection)url.openConnection();
                    conn.setDoInput(true);
                    conn.connect();

                    InputStream is = conn.getInputStream();
                    bitmap = BitmapFactory.decodeStream(is);
                }catch (IOException ex){}
            }
        };
        t.start();
        try{
            t.join();
            imageView01.setImageBitmap(bitmap);
        }catch(InterruptedException e){}
    }
}
