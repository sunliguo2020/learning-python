package com.nb.s2long;

class EncryptUtils {

    static {
        System.loadLibrary("encrypt");
    }

    public static native int s1(int v1, int v2);

    public static native String s2(String origin);

    public static native String s3(String origin);

    public static native String s4(String origin);

    public static native String s5(String origin);

    public static native String s6(String origin);

    public static native String s7();

    public static native String s8();
}
