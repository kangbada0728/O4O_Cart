package com.example.jewi9.myapplicationo4o;

import android.annotation.SuppressLint;
import android.app.TabActivity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuInflater;
import android.widget.TabHost;
import android.view.Menu;

@SuppressWarnings("deprecation")
public class Swipe_Compare extends TabActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.swipe_compare);

        TabHost comparTab = getTabHost(); //탭호스트 객체 생성
        TabHost.TabSpec spec;
        Intent intent;
        //가격 비교 탭!
        intent = new Intent(this, Compare.class);
        spec = comparTab.newTabSpec("FirstTab").setIndicator("가격비교").setContent(intent);
        comparTab.addTab(spec);

        //인기 상품 탭!
        intent = new Intent(this, Popular.class);
        spec = comparTab.newTabSpec("SecondTab").setIndicator("인기상품").setContent(intent);
        comparTab.addTab(spec);
    }

    @SuppressLint("ResourceType")
    @Override
    public boolean onCreateOptionsMenu(Menu menu)
    {
        //MenuInflater inflater = getMenuInflater();
        getMenuInflater().inflate(R.menu.swipe_compare,menu);
        return true;
    }
}