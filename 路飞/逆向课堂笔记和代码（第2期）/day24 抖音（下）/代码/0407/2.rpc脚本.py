import frida
import gzip

rdev = frida.get_remote_device()
session = rdev.attach("com.ss.android.ugc.aweme")

scr = """
rpc.exports = {      
    //自定义一个方法，接收两个参数。 [1,2,31,33,12,31]
    ttencrypt:function(bArr,len){
         var res;

         Java.perform(function () {
         
            var EncryptorUtil = Java.use("com.bytedance.frameworks.encryptor.EncryptorUtil");  

            // 将bArr转换成Java的字节数组。
            var dataByteArray = Java.array('byte', bArr);

            // 调用native方法，并获取返回值。
            res = EncryptorUtil.ttEncrypt(dataByteArray,len);
            
         });

         return res;
    }
}
"""
script = session.create_script(scr)
script.load()


# 0.要加密的文本
body = "武沛齐"

# 1.对文本进行gzip压缩
gzip_body = gzip.compress(body.encode('utf-8'))

# 2.处理gzip（java和python的结果不一样）
bs = bytearray(gzip_body)
bs[3:10] = [0, 0, 0, 0, 0, 0, 0]

# 3.ttencrypt加密并获取密文
sign_byte_list = script.exports.ttencrypt(list(bs), len(bs))
print(sign_byte_list)

