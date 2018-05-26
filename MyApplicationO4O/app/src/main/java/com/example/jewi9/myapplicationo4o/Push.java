package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
/*푸시 알림이 왔을 경우 보이는 창*/
public class Push extends AppCompatActivity
{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.push);
    }
    public void onClickWatchCoupon(View view)//쿠폰보기를 눌렀을 경우 쿠폰목록으로 이동한다.
    {
        Intent intent = new Intent( Push.this, Coupon.class);
        startActivity( intent );
    }
    public void onClickCancel(View view) //쿠폰보기를 취소했을 경우 Menu로 돌아간다.
    {
        Intent intent = new Intent( Push.this, Menu.class);
        startActivity( intent );
    }
}