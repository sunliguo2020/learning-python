import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.zhihu.android")

scr = """
Java.perform(function () {
    var CloudIDHelper = Java.use("com.zhihu.android.cloudid.CloudIDHelper");

    CloudIDHelper.encrypt.implementation = function(str,str2,str3,str4,str5,str6,str7){
        console.log("参数str=",str);
        console.log("参数str2=",str2);
        console.log("参数str3=",str3);
        console.log("参数str4=",str4);
        console.log("参数str5=",str5);
        console.log("参数str6=",str6);
        console.log("参数str7=",str7);
        var res = this.encrypt(str,str2,str3,str4,str5,str6,str7);
        console.log("结果是：",res);
        return res;
    }

});
"""

script = session.create_script(scr)


def on_message(message, data):
    pass


script.on("message", on_message)
script.load()
sys.stdin.read()


