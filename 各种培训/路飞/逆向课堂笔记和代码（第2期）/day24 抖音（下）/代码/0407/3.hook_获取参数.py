import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.ss.android.ugc.aweme")

scr = """
Java.perform(function () {

    function showMap(title,map){
        var result = "";
        
        var keyset = map.keySet();
        var it = keyset.iterator();
        while(it.hasNext()){
            var keystr = it.next().toString();
            var valuestr = map.get(keystr).toString();
            result += keystr;
            result += "=";
            result += valuestr;
            result += "; ";
        }
        console.log(title, result);
    }
    
    var tt1 = Java.use("com.ss.sys.ces.gg.tt$1");
    
    
    tt1.a.implementation = function(str,header){
        console.log('参数1->',str);
        showMap("参数2->",header);

        var res = this.a(str,header);

        console.log('-------------');
        return res;
    }
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message['payload'])


script.on("message", on_message)
script.load()
sys.stdin.read()


