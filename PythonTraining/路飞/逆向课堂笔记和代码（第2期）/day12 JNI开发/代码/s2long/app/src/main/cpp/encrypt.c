//
// Created by 武沛齐 on 2/24/22.
//
#include <jni.h>
#include <string.h>
#include <stdio.h>

JNIEXPORT jint
JNICALL Java_com_nb_s2long_EncryptUtils_s1(JNIEnv *env, jclass obj, jint v1, jint v2) {
    return v1 + v2;
}


JNIEXPORT jstring
JNICALL Java_com_nb_s2long_EncryptUtils_s2(JNIEnv *env, jclass obj, jstring origin) {
    char data[] = "hello";
    // C语言中的字符串转换成jstring
    jstring response = (*env)->NewStringUTF(env, data);
    return response; // jstring -> Java的字符串
}

JNIEXPORT jstring
JNICALL Java_com_nb_s2long_EncryptUtils_s3(JNIEnv *env, jclass obj, jstring origin) {
    // 获取参数中传入的字符串
    const char *string = (*env)->GetStringUTFChars(env, origin, 0);

    char data[4] = {string[0], string[2], string[4]}; // wpi

    // C语言中的字符串转换成jstring
    jstring response = (*env)->NewStringUTF(env, data);
    return response; // jstring -> Java的字符串
}


JNIEXPORT jstring
JNICALL Java_com_nb_s2long_EncryptUtils_s4(JNIEnv *env, jclass obj, jstring origin) {
    // 获取参数中传入的字符串
    const char *string = (*env)->GetStringUTFChars(env, origin, 0);

    char *data = "root";
    char buffer[100] = {};

    strcat(buffer, string);
    strcat(buffer, data);

    // C语言中的字符串转换成jstring
    jstring response = (*env)->NewStringUTF(env, buffer);
    return response; // jstring -> Java的字符串
}


JNIEXPORT jstring
JNICALL Java_com_nb_s2long_EncryptUtils_s5(JNIEnv *env, jclass obj, jstring origin) {
    char v34[80]; // ['0','1',,,,,,,,,]
    char *v28 = (char *) &v34;

    sprintf(v28, "%02x", 1);  // 01
    v28 += 2;

    sprintf(v28, "%02x", 2);  // 02
    v28 += 2;

    sprintf(v28, "%02x", 9);  // 09
    v28 += 2;

    sprintf(v28, "%02x", 12);  // 0b
    v28 += 2;

    sprintf(v28, "%02x", 20);  // 14
    v28 += 2;

    sprintf(v28, "%02x", 'a');  // 'a'字符  十进制 97  十六进制61

    // C语言中的字符串转换成jstring
    jstring response = (*env)->NewStringUTF(env, v34);
    return response; // jstring -> Java的字符串
}


JNIEXPORT jstring
JNICALL Java_com_nb_s2long_EncryptUtils_s6(JNIEnv *env, jclass obj, jstring origin) {
    // char v36[] = {'a', 'b', 'c', 'd', 'e', 'f'};   // 616263646566
    const char *v36 = (*env)->GetStringUTFChars(env, origin, 0);
    const int size = (*env)->GetStringLength(env, origin);

    char v34[80]; // [6,1,,,,,,,,]
    char *v28 = (char *) &v34;

    int v29 = 0;
    do {
        sprintf(v28, "%02x", v36[v29++]);
        v28 += 2;
    } while (v29 != size);

    // C语言中的字符串转换成jstring
    jstring response = (*env)->NewStringUTF(env, v34);
    return response; // jstring -> Java的字符串
}


JNIEXPORT jstring
JNICALL Java_com_nb_s2long_EncryptUtils_s7(JNIEnv *env, jclass obj) {
    char buffer[100] = {};

    char *data = "root";

    // 调用Java中的某个类中的某个静态方法，获取值。
    // 找到类
    jclass cls = (*env)->FindClass(env, "com/nb/s2long/DbHelper");

    // 类中找方法（静态方法）
    jmethodID method = (*env)->GetStaticMethodID(env, cls, "getPrev", "()Ljava/lang/String;");

    // 执行方法
    jstring res = (*env)->CallStaticObjectMethod(env, cls, method);

    // C语言的字节数组
    const char *string = (*env)->GetStringUTFChars(env, res, 0);

    strcat(buffer, data);
    strcat(buffer, string);

    // C语言中的字符串转换成jstring
    jstring response = (*env)->NewStringUTF(env, buffer);
    return response; // jstring -> Java的字符串
}


JNIEXPORT jstring
JNICALL Java_com_nb_s2long_EncryptUtils_s8(JNIEnv *env, jclass obj) {
    char buffer[100] = {};

    char *data = "root";

    // 调用Java中的某个类中的某个静态方法，获取值。
    // 找到类
    jclass cls = (*env)->FindClass(env, "com/nb/s2long/DbHelper");


    // 类中找方法（静态方法）
    jmethodID method1 = (*env)->GetStaticMethodID(env, cls, "getPrev", "()Ljava/lang/String;");
    // 执行方法
    jstring res1 = (*env)->CallStaticObjectMethod(env, cls, method1);
    // C语言的字节数组
    const char *string1 = (*env)->GetStringUTFChars(env, res1, 0);

    // 类中找方法（静态方法）
    jmethodID method2 = (*env)->GetStaticMethodID(env, cls, "getEnding",
                                                  "(Ljava/lang/String;II)Ljava/lang/String;");
    // 执行方法
    jstring res2 = (*env)->CallStaticObjectMethod(env, cls, method2,
                                                  (*env)->NewStringUTF(env, "xxx"), 11, 22);
    // C语言的字节数组
    const char *string2 = (*env)->GetStringUTFChars(env, res2, 0);


    // 找到FileHelper实例化并执行他的getData
    jclass cls2 = (*env)->FindClass(env, "com/nb/s2long/FileHelper");
    // 先找构造方法
    jmethodID init = (*env)->GetMethodID(env, cls2, "<init>", "(II)V");

    // 实例化对象
    jobject cls_obj = (*env)->NewObject(env, cls2, init, 11, 22);

    // 找getData方法
    jmethodID mid = (*env)->GetMethodID(env, cls2, "getData", "()Ljava/lang/String;");

    // 执行方法
    jstring res3 = (*env)->CallObjectMethod(env,cls_obj,mid);
    const char *string3 = (*env)->GetStringUTFChars(env, res3, 0);


    strcat(buffer, data);
    strcat(buffer, string1);
    strcat(buffer, string2);
    strcat(buffer, string3);

    // C语言中的字符串转换成jstring
    jstring response = (*env)->NewStringUTF(env, buffer);
    return response; // jstring -> Java的字符串
}