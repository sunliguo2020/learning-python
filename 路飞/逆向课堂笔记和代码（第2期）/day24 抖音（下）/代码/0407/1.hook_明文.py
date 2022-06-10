import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.ss.android.ugc.aweme")

scr = """
Java.perform(function () {
    var AppLog = Java.use("com.ss.android.common.applog.AppLog");
    
    AppLog.getLogEncryptSwitch.implementation = function(){
        var res = this.getLogEncryptSwitch();
        console.log(res);
        return false;
    }
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)
script.load()
sys.stdin.read()
