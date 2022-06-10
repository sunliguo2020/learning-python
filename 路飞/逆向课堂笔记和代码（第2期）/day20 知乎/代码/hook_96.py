import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.zhihu.android")

scr = """
Java.perform(function () {
    var HashMap = Java.use("java.util.HashMap");

    HashMap.put.implementation = function(key,value){
        if(key == "x-zse-96"){
            console.log(key,value);
            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
        }

        var res = this.put(key,value);

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
