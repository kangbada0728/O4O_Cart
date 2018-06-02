package com.example.jewi9.myapplicationo4o;

import android.content.Context;
import android.util.AttributeSet;
import android.widget.CheckBox;
import android.widget.Checkable;
import android.widget.LinearLayout;

import java.util.jar.Attributes;

public class CheckableLinearLayout extends LinearLayout implements Checkable {
    public CheckableLinearLayout(Context context, AttributeSet attrs) {
        super(context,attrs);
    }

    @Override
    public void setChecked(boolean checked) {//checked상태를 checked 변수대로 설정
        CheckBox cb = (CheckBox) findViewById(R.id.checkBox1) ;

        if (cb.isChecked() != checked) {
            cb.setChecked(checked) ;
        }
    }

    @Override
    public boolean isChecked() {//현재 check상태를 리턴하는 함수
        CheckBox cb = (CheckBox) findViewById(R.id.checkBox1) ;

        return cb.isChecked() ;
    }

    @Override
    public void toggle() {//현재 check상태를 바꿈
        CheckBox cb = (CheckBox) findViewById(R.id.checkBox1) ;

        setChecked(cb.isChecked() ? false : true) ;

    }
}
