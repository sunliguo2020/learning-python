package com.nb.s2long;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        // 当页面加载时，自动执行
        int v1 = EncryptUtils.s1(11, 22);
        Log.e("v1是", String.valueOf(v1)); // v1=33

        String v2 = EncryptUtils.s2("wupeiqi");
        Log.e("v2是", String.valueOf(v2));

        String v3 = EncryptUtils.s3("wupeiqi");
        Log.e("v3是", String.valueOf(v3)); // v1=33

        String v4 = EncryptUtils.s4("wupeiqi");
        Log.e("v4是", String.valueOf(v4)); // v1=33

        String v5 = EncryptUtils.s5("wupeiqi");
        Log.e("v5是", String.valueOf(v5));

        String v6 = EncryptUtils.s6("wupeiqi");
        Log.e("v6是", String.valueOf(v6)); // 77757065697169


        String v7 = EncryptUtils.s7();
        Log.e("v7是", String.valueOf(v7));

        String v8 = EncryptUtils.s8();
        Log.e("v8是", String.valueOf(v8));


        int v9 = DynamicUtils.add(11,2);
        Log.e("v9是", String.valueOf(v9));
    }


}