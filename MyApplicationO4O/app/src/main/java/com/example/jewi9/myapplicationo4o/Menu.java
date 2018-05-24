package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

public class Menu extends AppCompatActivity
{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.menu);

        /*Button btn_compare = (Button)findViewById(R.id.compareProduct);
        btn_compare.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });*/
    }

    /**/
    public void onClickCompare(View view) {
        Intent intent = new Intent(Menu.this, Compare.class);
        startActivity(intent);
    }
    public void onClickCoupon(View view)
    {
        Intent intent = new Intent( Menu.this, Coupon.class);
        startActivity( intent );
    }
}