package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class CompletePayment extends AppCompatActivity{
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.completepayment);

        TextView textview_price;
        Intent intent = getIntent();
        String price = intent.getStringExtra("price");

        textview_price = (TextView)findViewById(R.id.text2);
        textview_price.setText(price);

    }
}
