package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;


public class CheckWatchAd extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.check_watch_ad);
    }

    /*광고 보기를 취소했을 때*/
    public void onClickCancelCheckAD(View view)
    {
        Intent intent = new Intent( CheckWatchAd.this, Menu.class);
        startActivity( intent );
    }
    /*광고보기를 클릭했을 때*/
    public void onClickCheckAD(View view)
    {
        Intent intent = new Intent( CheckWatchAd.this, ShowAdPicture.class);
        startActivity( intent );
    }

}
