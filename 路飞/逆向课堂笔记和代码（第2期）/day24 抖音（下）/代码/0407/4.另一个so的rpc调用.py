import frida
import time

rdev = frida.get_remote_device()
session = rdev.attach("com.ss.android.ugc.aweme")

scr = """
rpc.exports = {   
    execandleviathan: function (i2,str){
        var result;
        Java.perform(function () {
            // 先处理拼接好的数据（字节数组） m44418a方法
            var bArr = [];
            for(var i=0;i<str.length;i+=2){
                var item = (parseInt(str[i],16) << 4) + parseInt(str[i+1],16);
                bArr.push(item);
            }

            // 转换为java的字节数组
            var dataByteArray = Java.array('byte',bArr);

            // 调用leviathan方法
            var Gorgon = Java.use("com.ss.sys.ces.a");
            result = Gorgon.leviathan(-1, i2 , dataByteArray);   //leviathan为方法名
        });
        return result;
    }
}
"""
script = session.create_script(scr)
script.load()

khronos = int(time.time())
un_sign_string = '6c2a0c5df32f1c2dcf537cb1b7c3c28a0000000000000000000000000000000054807aabff5a113a220938e77db4058d00000000000000000000000000000000'

sign_byte_list = script.exports.execandleviathan(khronos, un_sign_string)

print(sign_byte_list)
